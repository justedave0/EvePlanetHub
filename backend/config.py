from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    app_name: str = "EvePlanetHub API"
    environment: str = os.getenv("ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/eveplanethub")

    class Config:
        env_file = ".env"

settings = Settings()