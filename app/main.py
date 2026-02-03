from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import health_router
from app.api.v1.router import api_router

app = FastAPI(
    title="WAY Rental AI Services",
    description="AI 기반 렌터카 서비스",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(health_router, tags=["Health"])
app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
