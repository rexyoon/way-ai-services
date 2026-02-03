from fastapi import APIRouter, HTTPException
from app.schemas.pricing import PricingRequest, PricingResponse, PricingStrategy
from services.pricing.service import pricing_service

router = APIRouter()

@router.post("/calculate", response_model=PricingResponse)
async def calculate_price(request: PricingRequest):
    """가격 계산"""
    try:
        result = await pricing_service.calculate_price(
            product_id=request.product_id,
            base_price=request.base_price,
            strategy=request.strategy
        )
        return PricingResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/strategies")
async def get_strategies():
    """사용 가능한 가격 전략 목록"""
    return {
        "strategies": [
            {"name": "dynamic", "description": "수요 기반 동적 가격"},
            {"name": "fixed", "description": "고정 가격"},
            {"name": "discount", "description": "할인 가격"}
        ]
    }
