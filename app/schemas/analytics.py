from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

# 분석 요청
class AnalyticsRequest(BaseModel):
    user_id: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    metrics: List[str] = ["views", "clicks", "conversions"]

# 분석 결과 ← 이게 꼭 있어야 함!
class AnalyticsResponse(BaseModel):
    period: Dict[str, datetime]
    metrics: Dict[str, float]
    trends: Optional[List[Dict]] = None
    generated_at: datetime = Field(default_factory=datetime.utcnow)
