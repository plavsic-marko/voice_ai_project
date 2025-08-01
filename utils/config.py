from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DEEPGRAM_API_KEY: str
    ELEVEN_API_KEY: str
    ANTHROPIC_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
