from datetime import date

from sqlalchemy import Column, Date, Integer, String

from app.database.base import Base


class ProductMove(Base):
    """Данные о перемещениях товаров между участниками."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    gtin: str = Column(String, nullable=False, index=True)
    prid: str = Column(String, nullable=False, index=True)
    sender_inn: str = Column(String, nullable=False, index=True)
    receiver_inn: str = Column(String, nullable=False, index=True)
    dt: date = Column(Date, nullable=False)
    cnt_moved: int = Column(Integer, nullable=False)
