from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
from app.api.v1 import auth, chatbot

# ===== 환경 변수 로드 =====
load_dotenv()

# ===== FastAPI 앱 초기화 =====
app = FastAPI(
    title="WAY 렌터카 API",
    description="WAY 렌터카 플랫폼 백엔드 API",
    version="1.0.0"
)

# ===== CORS 설정 =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Qdrant 클라이언트 초기화 =====
qdrant = QdrantClient("http://localhost:6333")
print("✅ Qdrant 클라이언트 초기화 완료!")

# ===== 라우터 등록 =====
app.include_router(auth.router, prefix="/api/v1")
app.include_router(chatbot.router, prefix="/api/v1")

# ===== 기본 라우트 =====

@app.get("/")
def root():
    return {"message": "WAY 렌터카 API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

