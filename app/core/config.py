# app/core/config.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import List

# Load .env file variables
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Personal Finance Manager API"
    API_V1_STR: str = "/api/v1"

    # Database Configuration
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "pfm_db")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Security / JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_very_secret_key_please_change_this") # KEEP THIS SECRET!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # Token validity: 30 minutes

    # CORS (Cross-Origin Resource Sharing) - Adjust as needed for your frontend
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"] # Example frontend origins

    class Config:
        case_sensitive = True
        # If you want to load directly from .env without os.getenv
        # env_file = ".env"

settings = Settings()