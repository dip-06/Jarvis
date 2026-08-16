from pywinauto import Desktop,Application
import pyautogui
import subprocess
from Desktop_application_control.find_path import get_app_path
from Desktop_application_control.normalize_app_name import normalize_app_name
import time



def launch_and_get_window(exe_path: str, args: list = None, timeout: float = 5, stabilize_time: float = 1.0):
    """
    Launches ANY app and returns its main window -- no title/process
    knowledge needed ahead of time. Handles launcher-stub apps (Notepad)
    and multi-window startup apps (VS Code splash -> main window) the same way.
    """
    existing_handles = {w.handle for w in Desktop(backend="uia").windows()}

    subprocess.Popen([exe_path, *(args or [])])

    start_time = time.time()
    last_new_handles = set()
    stable_since = None

    while time.time() - start_time < timeout:
        current_handles = {w.handle for w in Desktop(backend="uia").windows()}
        new_handles = current_handles - existing_handles

        if new_handles:
            if new_handles == last_new_handles:
                if stable_since is None:
                    stable_since = time.time()
                elif time.time() - stable_since > stabilize_time:
                    break  # window set hasn't changed in a while = fully loaded
            else:
                stable_since = None  # still changing (e.g. splash -> main window)
            last_new_handles = new_handles

        time.sleep(0.3)

    if not last_new_handles:
        raise RuntimeError(f"No new window appeared within {timeout}s for: {exe_path}")

    candidates = [Desktop(backend="uia").window(handle=h) for h in last_new_handles]
    visible = [w for w in candidates if w.is_visible()]
    if not visible:
        raise RuntimeError("New window(s) appeared but none are visible")

    # heuristic: the MAIN window is almost always the biggest one on screen
    def area(w):
        r = w.rectangle()
        return (r.right - r.left) * (r.bottom - r.top)

    main_window = max(visible, key=area)
    main_window.wait('visible', timeout=timeout)
    return main_window
# usage:

def search_and_get_window(window_name: str, timeout: float = 2.0):
    # 1. Capture existing windows before typing
    initial_handles = {w.handle for w in Desktop(backend="uia").windows()}
    
    pyautogui.press('win')
    pyautogui.write(window_name)
    pyautogui.press('enter')
    
    start_time = time.time()
    target = window_name.lower()
    start = time.perf_counter()
    # 2. Keep checking dynamically until timeout
    while time.time() - start_time < timeout:
        current_windows = Desktop(backend="uia").windows()
        
        # Filter for newly created windows dynamically
        new_windows = [w for w in current_windows if w.handle not in initial_handles]
        
        for window in new_windows:
            try:
                title = window.window_text()
                if target in title.lower():
                    print("Found title:", title)
                    print("PID:", window.process_id())
                    return window # SUCCESS: Window found and returned immediately!
            except Exception:
                continue # In case window is still initializing
                
        time.sleep(0.5) # Wait before checking for new handles again
    end = time.perf_counter()
    print(end-start)
    # 3. If loop finishes with no match found:
    print(f"Sorry Sir I misheard : '{window_name}'.")
    pyautogui.press('esc') # Dismiss Start menu if it remained open
    return None

def open_app(voice_command):
    # plain_text_refine = voice_command.lower().removeprefix("open").strip()
    query = normalize_app_name(voice_command)
    try:
        PATH = get_app_path(query)
        window = launch_and_get_window(PATH)
    except (FileNotFoundError, RuntimeError):
        window = search_and_get_window(query)
    if window:
        window.set_focus()
        return window
        