from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
# 요청 모델
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    context: Optional[List[str]] = []
# 응답 모델
class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: str = "success"
# 대화 히스토리
class ChatHistory(BaseModel):
    user_id: str
    messages: List[dict]
    created_at: datetime
