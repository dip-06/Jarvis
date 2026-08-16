import time
import webbrowser
from Desktop_application_control import state
from keyboard_operation.key_combinations import toggle_view
from web_works.normalize_web_name import normalize_web_name
from web_works.common_web import websites
def visit_web(voice_command):
    
    target_site = normalize_web_name(voice_command)
    if state.in_toggle_view:
            toggle_view()
            time.sleep(0.3)
    if target_site in websites:
        webbrowser.open(websites[target_site])
    else:
        print(f"[Web] Unknown website keyword: '{target_site}'")