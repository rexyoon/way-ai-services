from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

#추천 요청
class RecommendationRequest(BaseModel):
    user_id: str
    category: Optional[str] = None
    limit: int = Field(default=10, ge=1, le=50)
#추천 아이템
class RecommendationResponse(BaseModel):
    item_id: str
    name: str
    score: float = Field(..., ge=0, le=1)
    category: Optional[str] = None
#추천응답
class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[RecommendationResponse]
    generated_at: datetime = Field(default_factory=datetime.utcnow);