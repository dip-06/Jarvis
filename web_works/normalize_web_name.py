import re
def normalize_web_name(voice_command: str) -> str:
    # 1. Remove the prefix
    query = re.sub(r'^(visit|go|to|goto)\s+', '', voice_command, flags=re.IGNORECASE).strip()
    # 2. Convert to lowercase
    query = query.lower()
    # 3. Strip surrounding whitespace, trailing dots, and double dots
    query = query.strip(" .")
    query = query.replace(",","")
    phonetic_map = {
        # --- General, Search & AI Tools ---
        "cloud": "claude",
        "claud": "claude",
        "chat gpt": "chatgpt",
        "chat g p t": "chatgpt",
        "duck duck go": "duckduckgo",
        "duckduck go": "duckduckgo",
        "hugging face": "huggingface",
        "wolfram alpha": "wolframalpha",
        "wolf ram alpha": "wolframalpha",
        "per plex": "perplex",
        "perplexity": "perplex",
        "co pilot": "copilot",
    
        # --- Developer Resources & Platforms ---
        "git hub": "github",
        "git lab": "gitlab",
        "bit bucket": "bitbucket",
        "stack overflow": "stackoverflow",
        "lead cord": "leetcode",
        "leadcode": "leetcode",
        "leet code": "leetcode",
        "late code": "leetcode",
        "hacker rank": "hackerrank",
        "code wars": "codewars",
        "dev to": "dev.to",
        "dev dot to": "dev.to",
        "hash node": "hashnode",
        "rep lit": "replit",
        "code sandbox": "codesandbox",
        "w 3 schools": "w3schools",
        "w3 schools": "w3schools",
        "m d n": "mdn",
        "mozilla developer network": "mdn",
        "python docs": "python_docs",
        "python documentation": "python_docs",
        "py pi": "pypi",
        "pie pie": "pypi",
        "docker hub": "docker_hub",
        "n p m": "npm",
        "post man": "postman",
        "regex 101": "regex101",
        "reg ex 101": "regex101",
    
        # --- Cloud & Infrastructure ---
        "a w s": "aws",
        "amazon web services": "aws",
        "azure portal": "azure",
        "g c p": "gcp",
        "google cloud": "gcp",
        "digital ocean": "digitalocean",
        "cloud flare": "cloudflare",
    
        # --- Cybersecurity & CTF Platforms ---
        "try hack me": "tryhackme",
        "hack the box": "hackthebox",
        "port swigger": "portswigger",
        "pico ctf": "picoctf",
        "pico c t f": "picoctf",
        "virus total": "virustotal",
        "cve mitre": "cve_mitre",
        "exploit db": "exploit_db",
        "exploit d b": "exploit_db",
        "over the wire": "overthewire",
        "n v d": "nvd",
        "have i been pwned": "haveibeenpwned",
        "have i been pawned": "haveibeenpwned",
    
        # --- Social Media & Networking ---
        "insta": "instagram",
        "twitter": "x",
        "linked in": "linkedin",
        "face book": "facebook",
        "you tube": "youtube",
        "red dit": "reddit",
        "snap chat": "snapchat",
    
        # --- Productivity & Collaboration ---
        "can va": "canva",
        "a s a n a": "asana",
        "air table": "airtable",
        "ever note": "evernote",
        "to do ist": "todoist",
        "todo ist": "todoist",
    
        # --- Cloud Storage & Office ---
        "g drive": "gdrive",
        "google drive": "gdrive",
        "drop box": "dropbox",
        "one drive": "onedrive",
        "g docs": "gdocs",
        "google docs": "gdocs",
        "g sheets": "gsheets",
        "google sheets": "gsheets",
        "office 365": "office365",
        "i cloud": "icloud",
    
        # --- News & Reference ---
        "wiki": "wikipedia",
        "b b c": "bbc",
        "bbc news": "bbc",
        "c n n": "cnn",
        "ny times": "nytimes",
        "new york times": "nytimes",
    
        # --- Shopping ---
        "ali express": "aliexpress",
        "flip kart": "flipkart",
    
        # --- Streaming & Entertainment ---
        "spot if i": "spotify",
        "spotifi": "spotify",
        "prime video": "primevideo",
        "amazon prime": "primevideo",
        "disney plus": "disneyplus",
        "sound cloud": "soundcloud",
    
        # --- Finance ---
        "pay pal": "paypal",
        "coin base": "coinbase",
        "yahoo finance": "yahoofinance",
    
        # --- Maps & Travel ---
        "google maps": "googlemaps",
        "maps": "googlemaps",
        "air bnb": "airbnb",
        "sky scanner": "skyscanner",
    
        # --- Design & Writing Tools ---
        "grammar ly": "grammarly",
        }
    return phonetic_map.get(query, query)