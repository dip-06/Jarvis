"""
Jarvis - STT module (importable into main.py)

WHY THIS IS STRUCTURED AS A CLASS:
Loading the wake word model + Whisper model takes a few seconds. You only
want to pay that cost ONCE at startup, not every time you need a
transcription. The class loads everything in __init__ and keeps the mic
stream open, so every call to .listen() after that is fast.
"""

import time
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
import openwakeword
from openwakeword.model import Model as WakeWordModel
import pygame

# ---------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------
SAMPLE_RATE = 16000
WAKEWORD_FRAME_SIZE = 1280
WAKEWORD_THRESHOLD = 0.5
SILENCE_RMS_THRESHOLD = 0.04
SILENCE_SECONDS_TO_STOP = 1.25
MAX_COMMAND_SECONDS = 8


class JarvisSTT:
    def __init__(self, whisper_model_size: str = "base.en"):
        print("[Jarvis] Loading wake word model...")
        openwakeword.utils.download_models()  # no-op after the first run
        self.wake_model = WakeWordModel(wakeword_models=["hey_jarvis"])

        print("[Jarvis] Loading STT model...")
        self.whisper_model = WhisperModel(whisper_model_size, device="cpu", compute_type="int8")

        self.stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32")
        self.stream.start()

        print("[Jarvis] STT ready -- mic stream is open and staying open.\n")

    def _listen_for_wake_word(self) -> None:
        while True:
            frame, _ = self.stream.read(WAKEWORD_FRAME_SIZE)
            frame_int16 = (frame.flatten() * 32767).astype(np.int16)

            predictions = self.wake_model.predict(frame_int16)
            for _model_name, score in predictions.items():
                if score > WAKEWORD_THRESHOLD:
                    pygame.mixer.init()
                    pygame.mixer.music.load("./voices/start.mp3")
                    pygame.mixer.music.play()
                    print("[Jarvis] Wake word detected!")
                    self.wake_model.reset()
                    return

    def _record_command(self) -> np.ndarray:
        print("[Jarvis] Listening for your command...")
        recorded_chunks = []
        silence_start = None
        start_time = time.time()

        while True:
            frame, _ = self.stream.read(WAKEWORD_FRAME_SIZE)
            recorded_chunks.append(frame.copy())

            rms = np.sqrt(np.mean(frame.flatten() ** 2))

            if rms < SILENCE_RMS_THRESHOLD:
                if silence_start is None:
                    silence_start = time.time()
                elif time.time() - silence_start > SILENCE_SECONDS_TO_STOP:
                    break
            else:
                silence_start = None

            if time.time() - start_time > MAX_COMMAND_SECONDS:
                print("[Jarvis] Max recording length hit, stopping.")
                break

        return np.concatenate(recorded_chunks, axis=0).flatten()

    def _transcribe(self, audio: np.ndarray) -> str:
        segments, _info = self.whisper_model.transcribe(audio, language="en", beam_size=5)
        return " ".join(segment.text.strip() for segment in segments).strip()

    def listen(self) -> str:
        """
        Blocks until 'Hey Jarvis' + a command is spoken, then returns the
        transcribed text. Returns "" if the recording was too short/silent.
        """
        self._listen_for_wake_word()
        audio = self._record_command()

        if len(audio) < SAMPLE_RATE * 0.3:
            print("[Jarvis] Didn't catch anything.\n")
            return ""

        print("[Jarvis] Transcribing...")
        text = self._transcribe(audio)
        if text == "" or "You":
            pygame.mixer.init()
            pygame.mixer.music.load("./voices/no_input.mp3")
            pygame.mixer.music.play()
        print(f"[You said] {text}\n")
        return text

    def close(self) -> None:
        """Call this on shutdown to release the mic properly."""
        self.stream.stop()
        self.stream.close()