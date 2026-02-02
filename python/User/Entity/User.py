from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255))
    Login = Column(String(255))
    Password = Column(String(500))
    Blocked = Column(Boolean, default=False)
    Deleted = Column(Boolean, default=False)
    CreatedAt = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    UpdatedAt = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))