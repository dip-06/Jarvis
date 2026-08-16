"""
Jarvis — Piper TTS starter script
Voice: en_US-hfc_female-medium

SETUP (one-time):
------------------
1. pip install piper-tts sounddevice numpy

2. Download BOTH files for this voice (they must sit in the same folder):
   - en_US-hfc_female-medium.onnx
   - en_US-hfc_female-medium.onnx.json
   Get them from: https://huggingface.co/rhasspy/piper-voices
   (browse to: en / en_US / hfc_female / medium /)

3. Put both files in a "voices" folder next to this script, e.g.:
   jarvis/
     tts_piper_starter.py
     voices/
       en_US-hfc_female-medium.onnx
       en_US-hfc_female-medium.onnx.json

4. Run:  python tts_piper_starter.py
"""

import sys
from pathlib import Path
import time
import numpy as np
import sounddevice as sd
from piper import PiperVoice

# ---------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------
VOICE_DIR = Path("voices")
MODEL_PATH = VOICE_DIR / "en_US-hfc_female-medium.onnx"
CONFIG_PATH = VOICE_DIR / "en_US-hfc_female-medium.onnx.json"


def load_voice() -> PiperVoice:
    """Load the Piper voice model once at startup."""
    if not MODEL_PATH.exists() or not CONFIG_PATH.exists():
        print(f"[ERROR] Missing model files. Expected both:\n"
              f"  {MODEL_PATH}\n"
              f"  {CONFIG_PATH}\n"
              f"Download them from https://huggingface.co/rhasspy/piper-voices")
        sys.exit(1)

    print("[Jarvis] Loading voice model...")
    voice = PiperVoice.load(str(MODEL_PATH), config_path=str(CONFIG_PATH))
    print("[Jarvis] Voice model loaded.")
    return voice


def speak(voice: PiperVoice, text: str) -> None:
    """
    Synthesize `text` to audio and play it immediately.

    Current piper-tts (1.2+) makes voice.synthesize(text) return a
    GENERATOR of AudioChunk objects rather than writing into a wav file
    directly -- so we must iterate it and pull the PCM bytes ourselves.
    """
    sample_rate = voice.config.sample_rate
    pcm_chunks = []

    for audio_chunk in voice.synthesize(text):
        pcm_chunks.append(audio_chunk.audio_int16_bytes)

    audio_bytes = b"".join(pcm_chunks)
    audio_array = np.frombuffer(audio_bytes, dtype=np.int16)

    sd.play(audio_array, samplerate=sample_rate)
    sd.wait()  # block until playback finishes
