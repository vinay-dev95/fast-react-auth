# app/core/config.py
from pydantic_settings import BaseSettings  # ✅ FIXED

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI React Auth"
    VERSION: str = "1.0.0"
    SECRET_KEY: str = "supersecretkey"
    DATABASE_URL: str = "sqlite:///./test.db"

settings = Settings()
