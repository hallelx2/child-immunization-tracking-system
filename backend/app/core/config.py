#from pydantic import BaseSettings
import os
from pydantic_settings import BaseSettings
import secrets
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"

    MAIL_USERNAME: Optional[str | None] = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: Optional[str | None] = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: Optional[str | None] = os.getenv("MAIL_FROM")
    MAIL_PORT: Optional[str | int | None] = os.getenv("MAIL_PORT")
    MAIL_SERVER: Optional[str | None] = os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME: Optional[str | None] = os.getenv("MAIL_FROM_NAME")

    DATABASE_URL: Optional[str | None] = os.getenv("DATABASE_URL")

    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 7 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    JWT_ENCODE_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings() # type: ignore
