from pywinauto import Desktop
from Desktop_application_control.normalize_app_name import normalize_app_name
def get_window(query):
    for window in Desktop(backend="uia").windows():
        title = window.window_text()
        if query.lower() in title.lower():
            print(title)
            return window
    return None 
    
