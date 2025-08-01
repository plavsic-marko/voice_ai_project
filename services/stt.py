import os
from dotenv import load_dotenv
from deepgram import Deepgram
import aiofiles
import ffmpeg


load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
dg_client = Deepgram(DEEPGRAM_API_KEY)

#  Funkcija za transkripciju .wav fajla


async def transcribe_audio(file_path: str) -> str:
    print("🎧 Pozvana transkripcija za:", file_path)

    async with aiofiles.open(file_path, 'rb') as f:
        audio_data = await f.read()

    try:
        print("Šaljem Deepgram servisu...")

        response = await dg_client.transcription.prerecorded(
            {
                "buffer": audio_data,
                "mimetype": "audio/wav"
            },
            {
                "punctuate": True,
                "language": "en"
            }
        )

        print("📨 Odgovor Deepgram:", response)

        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        print("Transkript:", transcript)
        return transcript or "Nije prepoznat govor."

    except Exception as e:
        print("Greška prilikom transkripcije:", e)
        return "Deepgram nije vratio ispravan odgovor."


def convert_webm_to_wav(input_path: str, output_path: str) -> bool:
    try:
        print(f"Konvertujem {input_path} u {output_path}...")
        ffmpeg.input(input_path).output(
            output_path,
            format='wav',
            acodec='pcm_s16le',
            ac=1,
            ar='16000'
        ).run(overwrite_output=True)
        print(f"Konverzija završena: {output_path}")
        return True
    except Exception as e:
        print(f"Greška prilikom konverzije: {e}")
        return False
