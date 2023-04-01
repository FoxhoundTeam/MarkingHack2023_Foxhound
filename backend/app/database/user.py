from sqlalchemy import Column, Integer, String

from app.database.base import Base


class User(Base):
    """Пользователь."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    username: str = Column(String, unique=True, nullable=False)
    password_hash: str = Column(String, nullable=False)
