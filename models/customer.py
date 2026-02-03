from sqlalchemy import Column, String, Boolean, DateTime, Date, Enum, Integer
from sqlalchemy.sql import func
from app.core.database import Base
import enum

class MembershipTier(str, enum.Enum):
    BASIC = "BASIC"
    SILVER = "SILVER"
    GOLD = "GOLD"
    VIP = "VIP"

class Gender(str, enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class Customer(Base):
    __tablename__ = "customers"

    id = Column(String(36), primary_key=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(20))
    name = Column(String(100), nullable=False)
    birth_date = Column(Date)
    gender = Column(Enum(Gender))
    profile_image_url = Column(String(500))

    # 운전면허 정보
    driver_license_no = Column(String(50))
    license_issue_date = Column(Date)
    license_expiry_date = Column(Date)
    license_type = Column(String(20))

    # 멤버십
    membership_tier = Column(Enum(MembershipTier), default=MembershipTier.BASIC)
    total_points = Column(Integer, default=0)

    # 메타 정보
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    last_login_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
