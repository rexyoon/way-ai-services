from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ 핵심 수정: settings를 나중에 import (함수 내부에서)
engine = None
SessionLocal = None
Base = declarative_base()

def _init_db():
    """데이터베이스 초기화 (lazy initialization)"""
    global engine, SessionLocal

    if engine is None:
        from app.core.config import settings  # 여기서만 import

        engine = create_engine(
            settings.DATABASE_URL,
            pool_pre_ping=True,
            pool_recycle=300,
            echo=settings.DEBUG
        )

        SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )

    return engine, SessionLocal

def get_db():
    """데이터베이스 세션 제공"""
    _init_db()  # 초기화
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
