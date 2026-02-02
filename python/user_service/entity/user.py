from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    login = Column("Login", String(255))
    password = Column("Password", String(500))
    blocked = Column("Blocked", Boolean, default=False)
    deleted = Column("Deleted", Boolean, default=False)
    created_at = Column("CreatedAt", DateTime, default=(lambda: datetime.now(timezone.utc)))
    updated_at = Column("UpdatedAt", DateTime, default=(lambda: datetime.now(timezone.utc)), onupdate=(lambda: datetime.now(timezone.utc)))