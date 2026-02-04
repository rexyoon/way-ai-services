from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # MySQL Database
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "way_admin"
    MYSQL_PASSWORD: str = "1234"
    MYSQL_DATABASE: str = "way_rental"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # JWT
    SECRET_KEY: str = "123452131241512521414124"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # App
    APP_ENV: str = "development"
    DEBUG: bool = True

    # OpenAI API Key
    OPENAI_API_KEY: Optional[str] = None  # API 키 추가

    # AI 모델 설정 추가
    AI_MODEL: str = "gpt-3.5-turbo"  # 기본 모델 추가

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    class Config:
        env_file = ".env"
        extra = "ignore"  # 추가 환경변수 무시
        case_sensitive = False  # 대소문자 구분 안함

settings = Settings()
