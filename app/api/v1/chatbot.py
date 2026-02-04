from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.chatbot_service import chatbot_service

router = APIRouter(prefix="/chatbot", tags=["AI Chatbot"])


class ChatRequest(BaseModel):
    user_id: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "message": "SUV 추천해주세요"
            }
        }


class ChatResponse(BaseModel):
    user_id: str
    message: str
    response: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    🤖 AI 챗봇과 대화

    - 차량 추천
    - 가격 문의
    - 예약 관련 질문
    - 일반 고객 상담
    """
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="메시지를 입력해주세요")

    response = chatbot_service.get_response(
        user_id=request.user_id,
        message=request.message
    )

    return ChatResponse(
        user_id=request.user_id,
        message=request.message,
        response=response
    )


@router.post("/clear/{user_id}")
async def clear_chat_history(user_id: str):
    """대화 히스토리 초기화"""
    success = chatbot_service.clear_history(user_id)
    return {
        "success": success,
        "message": "대화 히스토리가 초기화되었습니다." if success else "히스토리가 없습니다."
    }
