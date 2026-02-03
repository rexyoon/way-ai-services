import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
class TestRecommendation:
    """추천 API 테스트"""
    def test_get_recommendations(self):
        """추천 조회 테스트"""
        response = client.post("/api/v1/recommendations/",json={"user_id": "test_user", "limit": 5} )
        assert response.status_code == 200
        data = response.json()
        assert "recommendations" in data
        assert len(data["recommendations"]) <= 5
    def test_get_recommendations_with_category(self):
        """카테고리별 추천 테스트"""
        response = client.post(
            "/api/v1/recommendations/",
            json={
                "user_id": "test_user",
                "category": "electronics",
                "limit": 3})
        assert response.status_code == 200
    def test_similar_items(self):
        """유사 상품 테스트"""
        response = client.get("/api/v1/recommendations/similar/P001")
        assert response.status_code == 200
        data = response.json()
        assert "similar_items" in data
