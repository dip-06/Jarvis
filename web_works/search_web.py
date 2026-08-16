import webbrowser
from Desktop_application_control.normalize_app_name import normalize_app_name
def web_search(voice_command):
    if voice_command.startswith("Search"):
        search_query= normalize_app_name(voice_command)
        search_query = voice_command.removeprefix("Search").strip()
        webbrowser.open(f"https://google.com/search?q={search_query}")
    else:
        search_query = voice_command
        webbrowser.open(f"https://google.com/search?q={search_query}")