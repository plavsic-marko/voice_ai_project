from fastapi import APIRouter, UploadFile, File
from services.stt import transcribe_audio
from services.llm import get_response
from services.tts import generate_speech
from utils.audio import convert_webm_to_wav
import os

router = APIRouter()


@router.post("/voice_chat")
async def voice_chat(file: UploadFile = File(...)):
    try:
        # 1. Snimi primljeni fajl
        input_path = f"cache/{file.filename}"
        wav_path = input_path.replace(".webm", ".wav")

        with open(input_path, "wb") as f:
            f.write(await file.read())

        # 2. Konvertuj webm u wav
        if not convert_webm_to_wav(input_path, wav_path):
            return {"error": "Konverzija nije uspela."}

        # 3. Transkribuj glas u tekst (STT)
        transcript = await transcribe_audio(wav_path)
        if not transcript or not transcript.strip():
            return {"error": "Transkripcija nije uspela ili je prazna."}

        # 4. Pošalji transkript GPT-u
        response = await get_response(transcript)
        if not response or not response.strip():
            return {"error": "LLM odgovor nije dobijen ili je prazan."}

        # 5. Pretvori tekst odgovora u govor (TTS)
        audio_path = await generate_speech(response)
        if not audio_path or not os.path.exists(audio_path):
            return {"error": "TTS generisanje nije uspelo."}

        # 6. Vrati rezultat (tekst i audio)
        return {
            "transcript": transcript,
            "response": response,
            "audio_url": f"/static/{os.path.basename(audio_path)}"
        }

    except Exception as e:
        print("Neočekivana greška u voice_chat:", e)
        return {"error": "Interna greška u voice_chat handleru."}
