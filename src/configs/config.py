import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", )
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    POSTGRES_PORT: int = int(os.environ.get("POSTGRES_PORT", 5432))
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")


settings = Settings()
