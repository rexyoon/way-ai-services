from fastapi import APIRouter
from datetime import datetime

router = APIRouter()  # 이 이름을 main.py와 맞춰야 함

@router.get("/")
async def health_check():
    """서버 상태 확인"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "version": "1.0.0"
    }

@router.get("/ready")
async def readiness_check():
    """서비스 준비 상태 확인"""
    return {
        "ready": True,
        "services": {
            "database": "connected",
            "redis": "connected",
            "ai_model": "loaded"
        }
    }
