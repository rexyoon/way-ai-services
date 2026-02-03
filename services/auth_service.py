from sqlalchemy.orm import Session
from datetime import datetime
import uuid
from typing import Optional

from models.customer import Customer
from app.schemas.auth import CustomerCreate
from app.core.security import get_password_hash, verify_password, create_access_token, create_refresh_token

class AuthService:

    @staticmethod
    def get_customer_by_email(db: Session, email: str) -> Optional[Customer]:
        """이메일로 고객 조회"""
        return db.query(Customer).filter(Customer.email == email).first()

    @staticmethod
    def get_customer_by_id(db: Session, customer_id: str) -> Optional[Customer]:
        """ID로 고객 조회"""
        return db.query(Customer).filter(Customer.id == customer_id).first()

    @staticmethod
    def create_customer(db: Session, customer_data: CustomerCreate) -> Customer:
        """새 고객 생성"""
        customer = Customer(
            id=str(uuid.uuid4()),
            email=customer_data.email,
            password_hash=get_password_hash(customer_data.password),
            name=customer_data.name,
            phone=customer_data.phone,
            birth_date=customer_data.birth_date
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    @staticmethod
    def authenticate_customer(db: Session, email: str, password: str) -> Optional[Customer]:
        """고객 인증"""
        customer = AuthService.get_customer_by_email(db, email)
        if not customer:
            return None
        if not verify_password(password, customer.password_hash):
            return None

        # 마지막 로그인 시간 업데이트
        customer.last_login_at = datetime.utcnow()
        db.commit()

        return customer

    @staticmethod
    def create_tokens(customer_id: str) -> dict:
        """토큰 생성"""
        token_data = {"sub": customer_id}
        return {
            "access_token": create_access_token(token_data),
            "refresh_token": create_refresh_token(token_data),
            "token_type": "bearer"
        }
