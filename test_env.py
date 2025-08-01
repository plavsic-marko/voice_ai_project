import os
from dotenv import load_dotenv

load_dotenv()

print(" API ključ:", os.getenv("DEEPGRAM_API_KEY"))
