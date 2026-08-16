import re
def normalize_app_name(voice_command: str) -> str:
    # 1. Remove the prefix
    query = re.sub(r'^(open|close|launch|search|find|start|Minimize|Maximize|Minimise|Maximise|Focus|visit|go|to|goto|focus)\s+', '', voice_command, flags=re.IGNORECASE).strip()
    # 2. Convert to lowercase
    query = query.lower()
    # 3. Strip surrounding whitespace, trailing dots, and double dots
    query = query.strip(" .")
    query = query.replace(",","")

    # 4. Remove spaces inside words like "note pad" -> "notepad"
    query = re.sub(r"\s+", "", query)
    # 5. Remove .exe if it was already appended
    query = re.sub(r"\.exe$", "", query)

    # Phonetic & Mishearing Alias Map
    phonetic_map = {
        # VS Code mishearings
        "vsboard": "code",
        "vs board": "code",
        "visboard": "code",
        "vscode": "code",
        "code": "code",
        "Code": "code",
        "cord": "code",
        "ford": "code",
        "vs cord": "code",
        "visualstudiocode": "code",
        
        # Brave Browser mishearings
        "breath": "brave",
        "Breath": "brave",
        "Breath.": "brave",
        "brave": "brave",
        "brave browser": "brave",
        "fire faults":"firefox",
        "fire fox":"firefox",
        
        # Notepad mishearings
        "nordpad": "notepad",
        "nodepad": "notepad",
        "note-pad": "notepad",
        "note pen": "notepad",
        
        # Chrome / Edge
        "edg": "msedge",

        #Linux
        "kali linux":"kali",
        "cali linux":"kali",
        "linux":"kali",
        "cali":"kali",
        
    }
    
    # Return mapped name if present, otherwise return cleaned query
    return phonetic_map.get(query, query)
    
