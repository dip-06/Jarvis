from STT import JarvisSTT
from TTS import speak,load_voice
# from web_works.web_visit import visit_web
# from web_works.search_web import web_search
# from Desktop_application_control.openapp import open_app
# from Desktop_application_control.closeapp import close_app,minimize_app,maximize_app,set_focus
from brain.dispatcher import execute_tool_calls
from brain.groq_brain import ask_groq_with_retry
def main():
    voice = load_voice()
    # 1. Initialize STT once (loads models into RAM)
    stt = JarvisSTT(whisper_model_size="base.en")

    print("[Main] System active! Waiting for wake word...\n")
    speak(voice,"Jarvis Active.")

    try:
        while True:
            # 2. This call BLOCKS until you say "Hey Jarvis" and give a command
            user_text = stt.listen()
            # 3. Handle empty captures (e.g. background click or false trigger)
            if (not user_text) or user_text=="You":
                continue
            # Handle tasks
            message = ask_groq_with_retry(user_text)
            if message.tool_calls:
                execute_tool_calls(message)

            # Example logic check:
            if "exit" in user_text.lower() or "stop" in user_text.lower():
                print("[Main] Shutdown command received.")
                break
    except KeyboardInterrupt:
        print("\n[Main] Terminated by user (Ctrl+C).")
    finally:
        # 4. Clean up audio stream resources cleanly on exit
        stt.close()
        print("[Main] Audio stream closed safely.")

if __name__ == "__main__":
    main()