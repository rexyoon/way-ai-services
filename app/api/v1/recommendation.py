from fastapi import APIRouter, HTTPException
from typing import Optional
from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)
from services.recommendation.service import recommendation_service

router = APIRouter()  # ← 이 이름이 'router'여야 함!

@router.post("/", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """사용자 맞춤 추천"""
    try:
        result = await recommendation_service.get_recommendations(
            user_id=request.user_id,
            category=request.category,
            limit=request.limit
        )
        return RecommendationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/similar/{item_id}")
async def get_similar_items(item_id: str, limit: int = 5):
    """유사 상품 추천"""
    try:
        items = await recommendation_service.get_similar_items(
            item_id=item_id,
            limit=limit
        )
        return {"item_id": item_id, "similar_items": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
