# Jarvis Build — README (why each choice was made)

This folder has two files that matter for building:
- **requirements.txt** — every package to install
- **workflow.txt** — the architecture and the order to build things in

This README is the "why," comparing what ChatGPT, Claude, and Gemini each
suggested and explaining what got kept, dropped, or merged.

## The core disagreement between the three answers
ChatGPT's answer suggested trying to run everything **fully local**, listing
various open LLMs as if a 7-30B model could run comfortably on your machine.
Claude and Gemini both correctly flagged the real blocker: **your laptop has
no dedicated GPU/VRAM** (Intel UHD only shares system RAM), so a fully-local
setup would feel sluggish, not "lightning fast" — a local 7-8B model on CPU
alone lands around 5-10 tokens/sec, a multi-second delay before Jarvis even
starts talking.

**Verdict: Claude and Gemini's hybrid-brain approach wins.** Free cloud
inference (Groq) for speed, small quantized local model as offline-only
backup. This is what's in requirements.txt / workflow.txt.

## Component-by-component reasoning

| Component | Chosen tool | Why |
|---|---|---|
| Wake word | openWakeWord | All three suggested it — free, tiny, no disagreement |
| Speech-to-Text | faster-whisper | Claude & Gemini both specifically called out this CPU-optimized build over plain Whisper (ChatGPT's pick) — genuinely faster on your hardware |
| Primary brain | Groq free API | Claude & Gemini agree — sub-second responses, generous free tier, this is what actually delivers "Stark speed" |
| Offline brain | llama.cpp + quantized Qwen2.5-7B or Phi-3.5-mini | Claude's specific model picks fit your 16GB RAM with headroom; Gemini's Ollama+OpenVINO idea is a valid alternative if you prefer a GUI model manager |
| TTS | Piper (or Kokoro) | All three suggested one of these two — either is fine, pick by ear |
| Browser/social automation | Playwright | Claude & Gemini both preferred it over ChatGPT's Selenium — more modern, less flaky |
| Messaging | Telegram Bot API + Playwright for WhatsApp Web | Claude's breakdown was the most honest here: WhatsApp has no free official personal API, so it has to be browser automation, not a clean API call |
| VM control | Paramiko (SSH into Kali VirtualBox) | **Gemini's unique contribution** — neither ChatGPT nor Claude addressed your VM setup at all, but it's a genuinely useful addition if you want Jarvis to manage your Kali box too |
| Memory | ChromaDB + sentence-transformers | Claude's suggestion — lightweight, CPU-friendly embeddings |
| UI | System tray (pystray) + PyQt6 status window | Claude's minimal approach — skips Electron's overhead entirely |

## What was left out and why
- ChatGPT's list of specific 2026-era open models (Gemma 4, GLM-5, Kimi K2.5,
  etc.) was left out of requirements.txt — these are presented as
  established facts but several are unverifiable/speculative model names,
  and none of them change the core hardware conclusion anyway.
- LangChain was deliberately skipped (Claude's point) — raw tool-call JSON
  from Groq's API is simpler and faster for a personal assistant at this
  scale; add LangChain later only if the routing logic gets complex enough
  to need it.

## One thing to decide yourself
Piper vs Kokoro for TTS, and Qwen2.5 vs Phi-3.5 vs Ollama+OpenVINO for the
offline model — these are genuine toss-ups where the three answers differed
on preference, not fact. Try both, pick whichever sounds/performs better on
your machine.
