from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import BaseWithID

if TYPE_CHECKING:
    from .participant import Participant
    from .product import Product


class ProductMove(BaseWithID):
    """Данные о перемещениях товаров между участниками."""

    dt: date = Column(Date, nullable=False)

    gtin: str = Column(String, ForeignKey("product.gtin"), nullable=False)
    product: "Product" = relationship("Product", back_populates="moves")

    sender_inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    sender: "Participant" = relationship("Participant", back_populates="sent_products")

    receiver_inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    receiver: "Participant" = relationship("Participant", back_populates="received_products")

    cnt_moved: int = Column(Integer, nullable=False)
