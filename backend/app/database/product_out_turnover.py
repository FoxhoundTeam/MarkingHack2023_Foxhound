from datetime import date

from sqlalchemy import Column, Date, Float, Integer, String

from app.database.base import Base
from app.enums import ProductOutTurnoverOperationType


class ProductOutTurnover(Base):
    """Данные о выводе товаров из оборота."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    dt: date = Column(Date, nullable=False)
    gtin: str = Column(String, nullable=False, index=True)
    prid: str = Column(String, nullable=False, index=True)
    inn: str = Column(String, nullable=False, index=True)
    id_sp: str = Column(String, nullable=False, index=True)
    type_operation: ProductOutTurnoverOperationType = Column(String, nullable=False)
    price: float = Column(Float, nullable=False)
    cnt: int = Column(Integer, nullable=False)
