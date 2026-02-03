from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum
class PricingStrategy(str, Enum):
    DYNAMIC = "dynamic"
    FIXED = "fixed"
    DISCOUNT = "discount"
# 가격 요청
class PricingRequest(BaseModel):
    product_id: str
    base_price: float = Field(..., gt=0)
    strategy: PricingStrategy = PricingStrategy.DYNAMIC
# 가격 응답
class PricingResponse(BaseModel):
    product_id: str
    original_price: float
    suggested_price: float
    discount_rate: Optional[float] = None
    strategy_applied: str
    calculated_at: datetime = Field(default_factory=datetime.utcnow)
