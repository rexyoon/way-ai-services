from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_token
from app.schemas.auth import (
    CustomerCreate,
    LoginRequest,
    TokenResponse,
    RefreshTokenRequest,
    CustomerResponse
)
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def register(customer_data: CustomerCreate, db: Session = Depends(get_db)):
    """회원가입"""
    # 이메일 중복 확인
    existing = AuthService.get_customer_by_email(db, customer_data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 등록된 이메일입니다."
        )

    customer = AuthService.create_customer(db, customer_data)
    return customer

@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    """로그인"""
    customer = AuthService.authenticate_customer(db, login_data.email, login_data.password)

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일 또는 비밀번호가 올바르지 않습니다.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not customer.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="비활성화된 계정입니다."
        )

    tokens = AuthService.create_tokens(customer.id)
    return tokens

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(refresh_data: RefreshTokenRequest, db: Session = Depends(get_db)):
    """토큰 갱신"""
    payload = decode_token(refresh_data.refresh_token)

    if not payload or payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 리프레시 토큰입니다."
        )

    customer_id = payload.get("sub")
    customer = AuthService.get_customer_by_id(db, customer_id)

    if not customer or not customer.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자를 찾을 수 없습니다."
        )

    tokens = AuthService.create_tokens(customer.id)
    return tokens
