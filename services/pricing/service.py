from typing import Optional
from datetime import datetime
from enum import Enum

class PricingStrategy(str, Enum):
    DYNAMIC = "dynamic"
    FIXED = "fixed"
    DISCOUNT = "discount"
class PricingService:
    def __init__(self):
        # 가격 조정 설정
        self.demand_multiplier = 1.0
        self.min_margin = 0.1  # 최소 마진 10%
        self.max_discount = 0.3  # 최대 할인 30%
    async def calculate_price(
            self,
            product_id: str,
            base_price: float,
            strategy: PricingStrategy = PricingStrategy.DYNAMIC
    ) -> dict:
        """가격 계산"""
        if strategy == PricingStrategy.DYNAMIC:
            result = await self._dynamic_pricing(product_id, base_price)
        elif strategy == PricingStrategy.DISCOUNT:
            result = await self._discount_pricing(product_id, base_price)
        else:
            result = await self._fixed_pricing(base_price)

        return {
            "product_id": product_id,
            "original_price": base_price,
            "suggested_price": result["price"],
            "discount_rate": result.get("discount_rate"),
            "strategy_applied": strategy.value,
            "calculated_at": datetime.utcnow()
        }
    async def _dynamic_pricing(
            self,
            product_id: str,
            base_price: float
    ) -> dict:
        """동적 가격 책정 (TODO: ML 모델 연동)"""
        # 임시 로직: 수요/시간 기반 조정
        hour = datetime.utcnow().hour
        # 피크 시간 (12-14, 19-21) 가격 인상
        if 12 <= hour <= 14 or 19 <= hour <= 21:
            multiplier = 1.1
        # 새벽 시간 할인
        elif 2 <= hour <= 6:
            multiplier = 0.9
        else:
            multiplier = 1.0
        suggested_price = round(base_price * multiplier, 2)
        discount_rate = round((1 - multiplier) * 100, 1) if multiplier < 1 else None
        return {
            "price": suggested_price,
            "discount_rate": discount_rate
        }
    async def _discount_pricing(
            self,
            product_id: str,
            base_price: float
    ) -> dict:
        """할인 가격 책정"""
        # 임시: 15% 할인
        discount_rate = 15.0
        suggested_price = round(base_price * (1 - discount_rate / 100), 2)
        return {
            "price": suggested_price,
            "discount_rate": discount_rate
        }
    async def _fixed_pricing(self, base_price: float) -> dict:
        """고정 가격"""
        return {
            "price": base_price,
            "discount_rate": None
        }
# 싱글톤 인스턴스
pricing_service = PricingService()
