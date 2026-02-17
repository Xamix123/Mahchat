from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean, DateTime, func
from user_service.entity.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user_service.entity.contact_info import ContactInfo


class User(Base):
    __tablename__ = "app_user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    contact_info: Mapped["ContactInfo"] = relationship(
    back_populates="user",
    uselist=False,
    cascade="all, delete-orphan"
)