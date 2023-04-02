from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, Float, ForeignKey, ForeignKeyConstraint, Integer, String
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

    gtin: str = Column(String, nullable=False)
    prid: str = Column(String, nullable=False)
    product: "Product" = relationship("Product", backref="out_turnovers", foreign_keys=[gtin, prid])

    inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    participant: "Participant" = relationship("Participant", backref="out_turnovers", foreign_keys=[inn])

    id_sp: str = Column(String, ForeignKey("salespoint.id_sp"), nullable=False)
    sales_point: "SalesPoint" = relationship("SalesPoint", backref="out_turnovers")

    type_operation: ProductOutTurnoverOperationType = Column(String, nullable=False)
    price: float = Column(Float, nullable=False)
    cnt: int = Column(Integer, nullable=False)

    __table_args__ = (ForeignKeyConstraint([gtin, prid], ["product.gtin", "product.inn"]), {})
