import redis
from typing import Optional
from app.config import settings

class RedisClient:
    def __init__(self):
        self.client: Optional[redis.Redis] = None
    def connect(self):
        """Redis 연결"""
        self.client = redis.Redis(
            host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=0,decode_responses=True)
        return self.client
    def get(self, key: str) -> Optional[str]:
        """값 조회"""
        if self.client:
            return self.client.get(key)
        return None
    def set(self, key: str, value: str, expire: int = 3600) -> bool:
        """값 저장 (기본 1시간 만료)"""
        if self.client:
            return self.client.setex(key, expire, value)
        return False
    def delete(self, key: str) -> bool:
        """값 삭제"""
        if self.client:
            return self.client.delete(key) > 0
        return False
    def close(self):
        """연결 종료"""
        if self.client:
            self.client.close()
# 싱글톤 인스턴스
redis_client = RedisClient()
