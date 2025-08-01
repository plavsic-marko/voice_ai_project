from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.staticfiles import StaticFiles
import os
from routes import voice

from routes import speak, transcribe

app = FastAPI(title="Voice AI System")


os.makedirs("cache", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost",
    "http://127.0.0.1"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(speak.router, tags=["Speak"])
app.include_router(transcribe.router, tags=["Transcribe"])
app.include_router(voice.router, tags=["Voice"])


@app.get("/")
async def root():
    return {"message": "Voice AI radi 🎤"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
