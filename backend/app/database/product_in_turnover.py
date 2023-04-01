from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import BaseWithID
from app.enums import ProductInTurnoverOperationType

if TYPE_CHECKING:
    from .participant import Participant
    from .product import Product


class ProductInTurnover(BaseWithID):
    """Данные о вводе товаров в оборот."""

    dt: date = Column(Date, nullable=False)

    gtin: str = Column(String, ForeignKey("product.gtin"), nullable=False)
    product: "Product" = relationship("Product", back_populates="in_turnovers")

    inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    participant: "Participant" = relationship("Participant", back_populates="in_turnovers")

    operation_type: ProductInTurnoverOperationType = Column(String, nullable=False)
    cnt: int = Column(Integer, nullable=False)
