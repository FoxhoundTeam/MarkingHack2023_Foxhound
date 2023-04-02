from datetime import date

from sqlalchemy import Column, Date, Integer, String

from app.database.base import Base
from app.enums import ProductInTurnoverOperationType


class ProductInTurnover(Base):
    """Данные о вводе товаров в оборот."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    gtin: str = Column(String, nullable=False, index=True)
    prid: str = Column(String, nullable=False, index=True)
    inn: str = Column(String, nullable=False, index=True)
    dt: date = Column(Date, nullable=False)
    operation_type: ProductInTurnoverOperationType = Column(String, nullable=False)
    cnt: int = Column(Integer, nullable=False)
