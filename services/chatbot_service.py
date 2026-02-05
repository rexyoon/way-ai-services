from openai import AsyncOpenAI  # ✅ 비동기 클라이언트로 변경
from app.core.config import settings
from app.prompts.system_prompt import RENTAL_CAR_SYSTEM_PROMPT
from typing import List, Dict

class ChatbotService:
    def __init__(self):
        # ✅ AsyncOpenAI 사용
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.AI_MODEL
        self.conversation_history: Dict[str, List] = {}

    # ✅ async로 변경
    async def get_response(self, user_id: str, message: str) -> str:
        """사용자 메시지에 대한 AI 응답 생성"""

        # 대화 히스토리 초기화 (사용자별)
        if user_id not in self.conversation_history:
            self.conversation_history[user_id] = [
                {"role": "system", "content": RENTAL_CAR_SYSTEM_PROMPT}
            ]

        # 사용자 메시지 추가
        self.conversation_history[user_id].append(
            {"role": "user", "content": message}
        )

        try:
            # ✅ await 추가
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history[user_id],
                temperature=0.7,
                max_tokens=500
            )

            # AI 응답 추출
            ai_message = response.choices[0].message.content

            # 대화 히스토리에 AI 응답 추가
            self.conversation_history[user_id].append(
                {"role": "assistant", "content": ai_message}
            )
            return ai_message

        except Exception as e:
            error_msg = f"죄송합니다. 일시적인 오류가 발생했습니다: {str(e)}"
            print(f"❌ 오류: {error_msg}")
            return error_msg

    def clear_history(self, user_id: str) -> bool:
        """대화 히스토리 초기화"""
        if user_id in self.conversation_history:
            self.conversation_history[user_id] = [
                {"role": "system", "content": RENTAL_CAR_SYSTEM_PROMPT}
            ]
            return True
        return False

# 싱글톤 인스턴스
chatbot_service = ChatbotService()
