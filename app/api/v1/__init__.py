from fastapi import APIRouter
from app.api.v1 import chatbot  # 🆕 추가

api_router = APIRouter()

# 기존 라우터들...
# api_router.include_router(auth.router)

# 🆕 챗봇 라우터 추가
api_router.include_router(chatbot.router)
