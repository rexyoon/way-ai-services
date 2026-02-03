import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAnalytics:
    """분석 API 테스트"""
    def test_get_analytics(self):
        """분석 데이터 조회 테스트"""
        response = client.post("/api/v1/analytics/",json={"metrics": ["views", "clicks"]})
        assert response.status_code == 200
        data = response.json()
        assert "metrics" in data
        assert "views" in data["metrics"]
    def test_get_summary(self):
        """요약 통계 테스트"""
        response = client.get("/api/v1/analytics/summary")
        assert response.status_code == 200
        data = response.json()
        assert "summary" in data
