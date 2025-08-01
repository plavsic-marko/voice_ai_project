import os
from fastapi import APIRouter, UploadFile, File
from services.stt import transcribe_audio, convert_webm_to_wav

router = APIRouter()


@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    print("📥 Fajl primljen:", file.filename)

    input_path = f"temp_{file.filename}"
    output_path = input_path.replace(".webm", ".wav")

    # 📁 Snimi originalni .webm fajl
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # 🔄 Konverzija u .wav
    if not convert_webm_to_wav(input_path, output_path):
        return {"transcript": "Greška prilikom konverzije."}

    # 📂 Provera postojanja fajlova (debug)
    print("📂 Postoje li fajlovi?", os.path.exists(
        input_path), os.path.exists(output_path))

    # 🧠 Transkribuj .wav fajl
    transcript = await transcribe_audio(output_path)

    # 🧹 Očisti privremene fajlove
    os.remove(input_path)
    os.remove(output_path)

    return {"transcript": transcript or "Nema transkripta."}
