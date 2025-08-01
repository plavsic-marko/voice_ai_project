from openai import AsyncOpenAI
from utils.config import settings
from dotenv import load_dotenv
import os

load_dotenv()


client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def get_response(prompt: str) -> str:
    """
    Poziva OpenAI GPT-4 sa datim promptom i vraća odgovor kao string.
    """
    try:
        print("Šaljem prompt GPT-4:", prompt)

        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Odgovaraj jasno, koncizno i ljubazno."},
                {"role": "user", "content": prompt}
            ]
        )

        message = response.choices[0].message.content.strip()
        print("GPT odgovor:", message)
        return message

    except Exception as e:
        print("Greška u GPT-4 odgovoru:", e)
        return "Došlo je do greške prilikom generisanja odgovora."
