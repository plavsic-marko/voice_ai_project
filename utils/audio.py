import ffmpeg


def convert_webm_to_wav(input_path: str, output_path: str) -> bool:
    try:
        print(f"🔄 Konvertujem {input_path} u {output_path}...")
        ffmpeg.input(input_path).output(
            output_path,
            format='wav',
            acodec='pcm_s16le',
            ac=1,
            ar='16000'
        ).run(overwrite_output=True)
        print(f"✅ Konverzija završena: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Greška prilikom konverzije: {e}")
        return False
