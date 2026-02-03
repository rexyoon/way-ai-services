from fastapi import APIRouter
router = APIRouter()
@router.get("/")
async def get_recommendations():
    return{"message": "추천 엔진 API", "recommendations":[]}