from fastapi import APIRouter
router = APIRouter()
@router.post("/")
async def chat():
    return{
        "message": "챗봇API", "response": "안녕하세요! WAY렌터카입니다!"
    }