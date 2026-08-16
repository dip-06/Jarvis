import time
from Desktop_application_control.get_window_object import get_window
from Desktop_application_control.normalize_app_name import normalize_app_name
from keyboard_operation.key_combinations import toggle_view
from Desktop_application_control import state
def close_app(voice_command):
    if state.in_toggle_view:
        toggle_view()
        time.sleep(0.3)
    query = normalize_app_name(voice_command)
    window = get_window(query)
    if window:
        window.close()
    else:
        print(f"[close_app] No window found matching: {query}")

def minimize_app(voice_command):
    if state.in_toggle_view:
        toggle_view()
        time.sleep(0.3)
    query = normalize_app_name(voice_command)
    window = get_window(query)
    if window:
        window.minimize()
    else:
        print(f"[minimize_app] No window found matching: {query}")
def maximize_app(voice_command):
    if state.in_toggle_view:
        toggle_view()
        time.sleep(0.3)
    query = normalize_app_name(voice_command)
    window = get_window(query)
    if window:
        window.maximize()
    else:
        print(f"[maximize_app] No window found matching: {query}")

def set_focus(voice_command):
    if state.in_toggle_view:
        toggle_view()
        time.sleep(0.3)
    query = normalize_app_name(voice_command)
    window = get_window(query)
    if window:
        window.set_focus()
    else:
        print(f"[set_focus] No window found matching: {query}")