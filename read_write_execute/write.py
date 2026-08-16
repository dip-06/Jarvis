import time
import pyautogui
from Desktop_application_control.openapp import open_app
def open_and_write(voice_command,text: str):
    open_app(voice_command)
    time.sleep(1.5)
    pyautogui.write(text,interval=0.02)
