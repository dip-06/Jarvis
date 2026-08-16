from brain.groq_brain import ask_groq
import json
from web_works.search_web import web_search
from web_works.web_visit import visit_web
from Desktop_application_control.openapp import open_app
from Desktop_application_control.closeapp import close_app,set_focus,maximize_app,minimize_app
from read_write_execute.write import open_and_write
from keyboard_operation.key_combinations import toggle_view,shift_next_window,previous_tab,next_tab
TOOL_MAP = {
    "open_app": lambda app_name: open_app(app_name),
    "close_app": lambda app_name: close_app(app_name),
    "minimize_app": lambda app_name: minimize_app(app_name),
    "maximize_app": lambda app_name: maximize_app(app_name),
    "set_focus": lambda app_name: set_focus(app_name),
    "web_search": lambda query: web_search(query),
    "visit_web": lambda query: visit_web(query),
    "open_and_write": lambda app_name,text: open_and_write(app_name,text),
    "toggle_view": lambda: toggle_view(),
    "shift_next_window": lambda number_of_steps: shift_next_window(number_of_steps),
    "previous_tab": lambda number_of_steps: previous_tab(number_of_steps),
    "next_tab": lambda number_of_steps: next_tab(number_of_steps),
}
def execute_tool_calls(message):
    for call in message.tool_calls:
        func = TOOL_MAP.get(call.function.name)
        if not func:
            continue
        args = json.loads(call.function.arguments)
        print(f"[Dispatcher] Calling {call.function.name}({args})")
        func(**args)
