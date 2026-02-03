from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth

app = FastAPI(
    title="WAY 렌터카 API",
    description="WAY 렌터카 플랫폼 백엔드 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "WAY 렌터카 API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
