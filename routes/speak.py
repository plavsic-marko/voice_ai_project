from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from services.tts import generate_speech

router = APIRouter()


@router.get("/speak")
async def speak(
    text: str = Query(..., description="Tekst za pretvaranje u govor"),
    voice_id: str = Query("EXAVITQu4vr4xnSDxMaL",
                          description="ID glasa (npr. Rachel ili Adam)")
):
    audio_path = await generate_speech(text, voice_id)
    audio_file = open(audio_path, "rb")
    return StreamingResponse(audio_file, media_type="audio/mpeg")
