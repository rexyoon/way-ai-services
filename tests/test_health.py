import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
class TestHealth:
    """헬스체크 테스트"""
    def test_health_check(self):
        """기본 헬스체크"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    def test_readiness_check(self):
        """준비 상태 체크"""
        response = client.get("/health/ready")
        assert response.status_code == 200
        assert response.json()["ready"] == True
