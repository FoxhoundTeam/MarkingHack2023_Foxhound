from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.enums import ProductOutTurnoverOperationType

if TYPE_CHECKING:
    from .participant import Participant
    from .product import Product
    from .sales_point import SalesPoint


class ProductOutTurnover(Base):
    """Данные о выводе товаров из оборота."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    dt: date = Column(Date, nullable=False)

    gtin: str = Column(String, ForeignKey("product.gtin"), nullable=False)
    product: "Product" = relationship("Product", back_populates="out_turnovers")

    inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    participant: "Participant" = relationship("Participant", back_populates="out_turnovers")

    id_sp: str = Column(String, ForeignKey("salespoint.id_sp"), nullable=False)
    sales_point: "SalesPoint" = relationship("SalesPoint", back_populates="out_turnovers")

    type_operation: ProductOutTurnoverOperationType = Column(String, nullable=False)
    price: float = Column(Float, nullable=False)
    cnt: int = Column(Integer, nullable=False)
