import httpx
import os
from uuid import uuid4
from pathlib import Path
from utils.config import settings

DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Rachel
STATIC_DIR = Path("static")
STATIC_DIR.mkdir(exist_ok=True)

MAX_FILES = 10


def cleanup_cache():
    files = sorted(STATIC_DIR.glob("*.mp3"), key=lambda f: f.stat().st_mtime)
    while len(files) > MAX_FILES:
        files[0].unlink()
        files.pop(0)


async def generate_speech(text: str, voice_id: str = None) -> str:
    cleanup_cache()

    if not voice_id:
        voice_id = DEFAULT_VOICE_ID

    output_path = STATIC_DIR / f"{uuid4().hex}.mp3"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": settings.ELEVEN_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            print("ElevenLabs greška:", response.text)
            return ""

        with open(output_path, "wb") as f:
            f.write(response.content)

        print("Audio generisan:", output_path)
        return str(output_path)

    except Exception as e:
        print("Greška u TTS:", e)
        return ""
