# Voice AI Chat

**Voice AI Chat** je jednostavna aplikacija koja omogućava korisnicima da razgovaraju sa AI-em putem glasa. Sistem koristi **STT (Speech-to-Text)**, **LLM (Language Model)** i **TTS (Text-to-Speech)** za obradu glasovne interakcije.

---

## Funkcionalnosti

- Snimi glas korisnika (WebM)
- Transkribuj govor koristeći Deepgram STT
- Pošalji transkript OpenAI GPT modelu
- Konvertuj AI odgovor u govor koristeći ElevenLabs TTS
- Prikaz transkripta, odgovora i audio plejera u browseru
- Fallback mehanizmi za greške u STT, LLM i TTS procesima
- Jednostavan frontend (HTML + CSS + JS)

---

## Tehnologije

- **FastAPI** – backend server
- **Deepgram** – STT servis (Speech-to-Text)
- **OpenAI GPT** – za generisanje odgovora
- **ElevenLabs** – za TTS (Text-to-Speech)
- **FFmpeg** – za konverziju webm → wav
- **Frontend** – HTML + CSS + JavaScript (fetch API)

---

## Instalacija

1. Kloniraj repozitorijum:

   ```bash
   git clone https://github.com/plavsi-marko/voice_ai_project.git
   cd voice_ai_project
   ```

2. Kreiraj virtualno okruženje:

   ```bash
   python -m venv venv
   source venv/bin/activate  # ili venv\Scripts\activate na Windows
   ```

3. Instaliraj zavisnosti:

   ```bash
   pip install -r requirements.txt
   ```

4. Kreiraj `.env` fajl u root folderu:

   ```env
   OPENAI_API_KEY=sk-...
   ELEVEN_API_KEY=...
   DEEPGRAM_API_KEY=...
   ```

5. Uveri se da imaš instaliran `ffmpeg` (dostupan iz komandne linije).

---

## Pokretanje aplikacije

1. Pokreni FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Pokreni lokalni frontend server:

   ```bash
   cd frontend
   python -m http.server 5173
   ```

3. Otvori frontend u browseru:

   ```
   http://localhost:5173/index.html
   ```

---

## Testiranje

- Klikni na dugme **"Snimi i razgovaraj s AI-em"**
- Sačekaj da se AI obradi snimak (cca 3–5 sekundi)
- Pojaviće se:
  - Transkript tvog glasa
  - AI odgovor
  - Audio plejbek odgovora

---

## Fallback mehanizmi

Sistem je robustan i podržava greške u sledećim komponentama:

| Komponenta | Fallback poruka                        |
| ---------- | -------------------------------------- |
| STT        | "Ne mogu da razumem glas."             |
| LLM        | "Nisam siguran kako da odgovorim."     |
| TTS        | "Odgovor nije moguće izgovoriti."      |
| Server     | "Greška pri komunikaciji sa serverom." |

---

## Struktura projekta

```
voice-ai-chat/
│
├── main.py
├── .env
├── requirements.txt
├── frontend/
│   └── index.html
├── cache/                # Privremeni fajlovi (audio)
├── routes/
│   ├── voice.py
│   ├── speak.py
│   └── transcribe.py
├── services/
│   ├── stt.py
│   ├── llm.py
│   └── tts.py
└── utils/
    ├── audio.py
    └── config.py
```

---

## Kontakt

Autor: [Marko Plavšić]
