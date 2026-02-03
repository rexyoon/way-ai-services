from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    # App
    APP_NAME: str = "WAY AI Services"
    DEBUG: bool = True

    # MySQL
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "way_admin"
    MYSQL_PASSWORD: str = "way_secret_2024"
    MYSQL_DATABASE: str = "way_rental"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    #API KEYS(추후 추가)
    # OPENAI_API_KEY: Optional[str] = None


    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
settings = get_settings()
