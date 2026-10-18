from sqlalchemy import Column, DateTime, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
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
    user_id: int = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
