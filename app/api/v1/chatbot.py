from fastapi import APIRouter, HTTPException
from app.schemas.chatbot import ChatRequest, ChatResponse
from services.chatbot.service import chatbot_service

router = APIRouter()

@router.post("/message", response_model=ChatResponse)
async def send_message(request: ChatRequest):
    """챗봇에게 메시지 전송"""
    try:
        result = await chatbot_service.generate_response(
            message=request.message,
            user_id=request.user_id,
            session_id=request.session_id,
            context=request.context
        )
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history/{session_id}")
async def get_history(session_id: str):
    """대화 히스토리 조회"""
    history = chatbot_service.get_session_history(session_id)
    return {"session_id": session_id, "messages": history}

@router.delete("/session/{session_id}")
async def clear_session(session_id: str):
    """세션 초기화"""
    success = chatbot_service.clear_session(session_id)
    if success:
        return {"message": "Session cleared", "session_id": session_id}
    raise HTTPException(status_code=404, detail="Session not found")
