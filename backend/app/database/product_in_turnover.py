from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.enums import ProductInTurnoverOperationType

if TYPE_CHECKING:
    from .participant import Participant
    from .product import Product


class ProductInTurnover(Base):
    """Данные о вводе товаров в оборот."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    dt: date = Column(Date, nullable=False)

    gtin: str = Column(String, nullable=False)
    prid: str = Column(String, nullable=False)
    product: "Product" = relationship("Product", backref="in_turnovers", foreign_keys=[gtin, prid])

    inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    participant: "Participant" = relationship("Participant", backref="in_turnovers", foreign_keys=[inn])

    operation_type: ProductInTurnoverOperationType = Column(String, nullable=False)
    cnt: int = Column(Integer, nullable=False)

    __table_args__ = (ForeignKeyConstraint([gtin, prid], ["product.gtin", "product.inn"]), {})
