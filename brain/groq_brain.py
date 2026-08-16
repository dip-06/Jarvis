from groq import Groq
import os
from brain.tools_schema import TOOLS
from dotenv import load_dotenv
from groq import BadRequestError
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = (
    "You are Jarvis, a voice assistant. If the user's request maps to one of your tools, call it , give JSON respone only. Otherwise reply naturally and briefly, like a spoken response, not a wall of text."
)

def ask_groq(user_text:str):
    responce = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        tools=TOOLS,
        tool_choice="auto",
        max_tokens=500
    
    )
    return responce.choices[0].message
def ask_groq_with_retry(user_text: str, retries=2):
    for attempt in range(retries + 1):
        try:
            return ask_groq(user_text)
        except BadRequestError as e:
            code = getattr(e, "body", {}).get("error", {}).get("code", "")
            if code == "tool_use_failed" and attempt < retries:
                print(f"[Groq] Tool call malformed (attempt {attempt+1}), retrying...")
                continue
            raise