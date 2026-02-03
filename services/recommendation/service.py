from typing import List, Optional
from datetime import datetime
import random

class RecommendationService:
    def __init__(self):
        # 임시 상품 데이터 (나중에 DB에서 가져옴)
        self.products = [
            {"item_id": "P001", "name": "스마트 워치", "category": "electronics", "score": 0.95},
            {"item_id": "P002", "name": "무선 이어폰", "category": "electronics", "score": 0.92},
            {"item_id": "P003", "name": "노트북 스탠드", "category": "accessories", "score": 0.88},
            {"item_id": "P004", "name": "기계식 키보드", "category": "electronics", "score": 0.85},
            {"item_id": "P005", "name": "모니터 암", "category": "accessories", "score": 0.82},
            {"item_id": "P006", "name": "USB 허브", "category": "accessories", "score": 0.78},
            {"item_id": "P007", "name": "웹캠", "category": "electronics", "score": 0.75},
            {"item_id": "P008", "name": "마우스 패드", "category": "accessories", "score": 0.72},
        ]
    async def get_recommendations(
            self,
            user_id: str,
            category: Optional[str] = None,
            limit: int = 10
    ) -> dict:
        """사용자 맞춤 추천 생성"""
        # 카테고리 필터링
        filtered_products = self.products
        if category:
            filtered_products = [
                p for p in self.products
                if p["category"] == category
            ]
        # TODO: 실제 ML 모델로 개인화 추천 구현
        recommendations = await self._generate_recommendations(
            user_id, filtered_products, limit
        )
        return {
            "user_id": user_id,
            "recommendations": recommendations,
            "generated_at": datetime.utcnow()
        }
    async def _generate_recommendations(
            self,
            user_id: str,
            products: List[dict],
            limit: int
    ) -> List[dict]:
        """추천 알고리즘 (TODO: ML 모델 연동)"""
        # 임시: 점수 기반 정렬 + 약간의 랜덤성
        shuffled = products.copy()
        for item in shuffled:
            item["score"] = round(item["score"] * random.uniform(0.9, 1.0), 2)
        sorted_products = sorted(
            shuffled,
            key=lambda x: x["score"],
            reverse=True
        )
        return sorted_products[:limit]
    async def get_similar_items(
            self,
            item_id: str,
            limit: int = 5
    ) -> List[dict]:
        """유사 상품 추천"""
        # 현재 아이템 찾기
        current_item = next(
            (p for p in self.products if p["item_id"] == item_id),
            None
        )
        if not current_item:
            return []
        # 같은 카테고리 상품 반환
        similar = [
            p for p in self.products
            if p["category"] == current_item["category"]
               and p["item_id"] != item_id]
        return similar[:limit]
# 싱글톤 인스턴스
recommendation_service = RecommendationService()
