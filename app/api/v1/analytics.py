from fastapi import APIRouter
router = APIRouter()
@router.get("/")
async def get_analytics():
    return{"message": "분석api", "data": {}}