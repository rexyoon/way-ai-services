from fastapi import APIRouter
from app.api.v1 import chatbot, recommendation, pricing, analytics

api_router = APIRouter()

api_router.include_router(
    chatbot.router,
    prefix="/chat",
    tags=["Chatbot"]
)

api_router.include_router(
    recommendation.router,    # ← 이게 있어야 함!
    prefix="/recommendations",
    tags=["Recommendations"]
)

api_router.include_router(
    pricing.router,
    prefix="/pricing",
    tags=["Pricing"]
)

api_router.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["Analytics"]
)
