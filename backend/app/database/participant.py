from sqlalchemy import Column, String

from app.database.base import Base


class Participant(Base):
    """Справочник участников оборота товаров."""

    inn: str = Column(String, primary_key=True, index=True, unique=True, nullable=False)
    region_code: str = Column(String, nullable=False)
