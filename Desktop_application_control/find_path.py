import os
import winreg

def is_valid_executable(path: str) -> bool:
    """Checks if the path exists, is a file, and has execute permissions."""
    if not path:
        return False
    
    # Strip quotes if the registry saved it like `"C:\path\app.exe"`
    clean_path = path.strip('"')
    
    # Verify file exists and is executable
    return os.path.isfile(clean_path) and os.access(clean_path, os.X_OK)


def get_app_path(app_name: str) -> str:
    """Finds the full executable path of an app from the Windows Registry."""
    if not app_name.endswith(".exe"):
        app_name += ".exe"
    
    key_path = fr"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\{app_name}"
    
    # Check HKEY_LOCAL_MACHINE & HKEY_CURRENT_USER
    for hkey in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        try:
            with winreg.OpenKey(hkey, key_path) as key:
                exe_path = winreg.QueryValue(key, None)
                
                # Check if file actually exists and works!
                if is_valid_executable(exe_path):
                    return exe_path.strip('"')
                else:
                    print(f"[!] Registry found path for '{app_name}', but file is missing/unusable: {exe_path}")
        except FileNotFoundError:
            continue
            
    raise FileNotFoundError(f"No valid/runnable executable found for '{app_name}'")