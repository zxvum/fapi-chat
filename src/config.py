import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str = '0.0.0.0'
    DB_PORT: str = 5432
    DB_NAME: str
    DB_USER: str
    DB_PASS: str


settings = Settings()
