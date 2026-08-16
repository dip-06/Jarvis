import pyautogui
from Desktop_application_control import state
def toggle_view():
    pyautogui.hotkey('win','tab')
    state.in_toggle_view = not state.in_toggle_view
def shift_next_window(number_of_steps:int):
    for steps in range(0,number_of_steps):
        pyautogui.hotkey('alt','tab')
def next_tab(number_of_steps:int):
    for steps in range(0,number_of_steps):
        pyautogui.hotkey('ctrl','tab')
def previous_tab(number_of_steps:int):
    for steps in range(0,number_of_steps):
        pyautogui.hotkey('ctrl','shift','tab')
