TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "open_app",
            "description": "Open a desktop application",
            "parameters": {
                "type": "object",
                "properties": {
                    "app_name": {"type": "string", "description": "Name of the app, e.g. 'chrome', 'notepad'. JSON format only, no XML"}
                },
                "required": ["app_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "close_app",
            "description": "Close/turn off/take down a currently open application. 'breath'='brave'",
            "parameters": {
                "type": "object",
                "properties": {
                    "app_name": {"type": "string", "description": "Name of the app, e.g. 'chrome', 'notepad'"}
                },
                "required": ["app_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string","description":"Search Query, e.g 'how to make pizza','pyautogui documentation' . strictly JSON format only. no XML"}},
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "visit_web",
            "description": "Search the web for an website and open it",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string","description":"Name of the website, e.g 'youtube','tryhackme','github'"}},
                "required": ["query"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "set_focus",
        "description": "Bring an already-open application's window to the foreground which means focus on the window",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app, e.g. 'chrome', 'notepad'"}
            },
            "required": ["app_name"]
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "minimize_app",
        "description": "Minimize an already-open application's window",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app, e.g. 'chrome', 'notepad'"}
            },
            "required": ["app_name"]
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "open_and_write",
        "description": "Open file or application and write.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string","type":"string", "description": "Name of the app, e.g. 'chrome', 'notepad' and the text to be written"}
            },
            "required": ["app_name","text"]
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "maximize_app",
        "description": "Maximize an already-open application's window",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app, e.g. 'chrome', 'notepad'"}
            },
            "required": ["app_name"]
        }
    },
    },

    {
    "type": "function",
    "function": {
        "name": "toggle_view",
        "description": "Show all opened window by windows default toggle view feature",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "shift_next_window",
        "description": "Go to the next opened window",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "integer", "description": "Number of times the function should be called. Return only integer e.g 0,1,2,3.. .If not specified then default is 0"}
            },
            "required": ["number_of_steps"]
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "previous_tab",
        "description": "Go to the previous tab",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "integer", "description": "Number of times the function should be called. Return only integer e.g 0,1,2,3.. .If not specified then default is 0"}
            },
            "required": ["number_of_steps"]
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "next_tab",
        "description": "Go to the next tab",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "integer", "description": "Number of times the function should be called. Return only integer e.g 0,1,2,3.. .If not specified then default is 0"}
            },
            "required": ["number_of_steps"]
        }
    },
    },


]