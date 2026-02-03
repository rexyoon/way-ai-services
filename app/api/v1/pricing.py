from fastapi import APIRouter
router = APIRouter()
@router.post("/predict")
async def predict_price():
    return{ "message": "가격 예측 API", "predicted_price": 50000}