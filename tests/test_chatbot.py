import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
class TestChatbot:
    """챗봇 API 테스트"""
    def test_send_message(self):
        """메시지 전송 테스트"""
        response = client.post( "/api/v1/chat/message", json={"message": "안녕하세요"})
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "session_id" in data
        assert data["status"] == "success"
    def test_send_message_with_user_id(self):
        """사용자 ID 포함 메시지 테스트"""
        response = client.post(
            "/api/v1/chat/message",
            json={"message": "추천해줘", "user_id": "test_user_123"})
        assert response.status_code == 200
    def test_empty_message(self):
        """빈 메시지 테스트"""
        response = client.post( "/api/v1/chat/message", json={"message": ""}
        )
        assert response.status_code == 422  # Validation error