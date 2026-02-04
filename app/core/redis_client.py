from redis import Redis
from app.core.config import settings  # 경로 통일

redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
    decode_responses=True
)
