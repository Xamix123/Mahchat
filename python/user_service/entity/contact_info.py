from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from user_service.entity.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user_service.entity.user import User
    from user_service.entity.contact_type import ContactType

class ContactInfo(Base):
    __tablename__ = "contact_info"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("app_user.id"),
        unique=True,
        nullable=False
    )

    contact_type_id: Mapped[int] = mapped_column(
        ForeignKey("contact_type.id"),
        unique=False,
        nullable=False
    )

    value: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="contact_info"
    )

    contact_type: Mapped["ContactType"] = relationship(
        "ContactType",
        back_populates="contact_info"
    )