import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPricing:
    """가격 API 테스트"""
    def test_calculate_dynamic_price(self):
        """동적 가격 계산 테스트"""
        response = client.post(
            "/api/v1/pricing/calculate",
            json={"product_id": "P001","base_price": 10000, "strategy": "dynamic"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "suggested_price" in data
        assert data["strategy_applied"] == "dynamic"
    def test_calculate_discount_price(self):
        """할인 가격 계산 테스트"""
        response = client.post(
            "/api/v1/pricing/calculate",
            json={"product_id": "P001","base_price": 10000, "strategy": "discount" } )
        assert response.status_code == 200
        data = response.json()
        assert data["discount_rate"] is not None
    def test_get_strategies(self):
        """전략 목록 조회 테스트"""
        response = client.get("/api/v1/pricing/strategies")
        assert response.status_code == 200
        assert "strategies" in response.json()
