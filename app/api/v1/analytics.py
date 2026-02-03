from fastapi import APIRouter, HTTPException
from typing import Optional, List
from datetime import datetime
from app.schemas.analytics import AnalyticsRequest, AnalyticsResponse
from services.analytics.service import analytics_service

router = APIRouter()

@router.post("/", response_model=AnalyticsResponse)
async def get_analytics(request: AnalyticsRequest):
    """분석 데이터 조회"""
    try:
        result = await analytics_service.get_analytics(
            user_id=request.user_id,
            start_date=request.start_date,
            end_date=request.end_date,
            metrics=request.metrics
        )
        return AnalyticsResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/summary")
async def get_summary():
    """간단한 요약 통계"""
    try:
        result = await analytics_service.get_analytics(
            metrics=["views", "clicks", "conversions", "revenue"]
        )
        return {
            "summary": result["metrics"],
            "generated_at": datetime.utcnow()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
