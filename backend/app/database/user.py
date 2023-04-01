from sqlalchemy import Column, String

from app.database.base import BaseWithID


class User(BaseWithID):
    """Пользователь."""

    username: str = Column(String, unique=True, nullable=False)
    password_hash: str = Column(String, nullable=False)
