from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from user_service.entities.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user_service.entities.contact_info import ContactInfo


class ContactType(Base):
    __tablename__ = "contact_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)

    contact_info: Mapped[list["ContactInfo"]] = relationship(
        back_populates="contact_type"
    )
