from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

# 회원가입
class CustomerCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    name: str = Field(..., min_length=2, max_length=100)
    phone: Optional[str] = None
    birth_date: Optional[date] = None

# 로그인
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# 토큰 응답
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

# 토큰 갱신 요청
class RefreshTokenRequest(BaseModel):
    refresh_token: str

# 사용자 정보 응답
class CustomerResponse(BaseModel):
    id: str
    email: str
    name: str
    phone: Optional[str]
    membership_tier: str
    total_points: int
    is_verified: bool

    class Config:
        from_attributes = True
