from fastapi import APIRouter
from app.api.v1 import recommendation, chatbot, pricing, analytics
api_router = APIRouter()
api_router.include_router(recommendation.router, prefix="/recommendation", tags=["Recommendation"])
api_router.include_router(chatbot.router, prefix="/chat", tags=["Chatbot"])
api_router.include_router(pricing.router, prefix="/pricing", tags=["Pricing"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
