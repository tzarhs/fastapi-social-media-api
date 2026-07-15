from sqlalchemy import Column, DateTime, String, Boolean, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id: int | None = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String, index=True, nullable=False)
    content: str = Column(String, index=True, nullable=False)
    published: bool = Column(Boolean, server_default='TRUE', nullable=False)
    created_at: DateTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))