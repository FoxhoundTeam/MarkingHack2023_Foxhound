from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from .participant import Participant
    from .product import Product


class ProductMove(Base):
    """Данные о перемещениях товаров между участниками."""

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)
    dt: date = Column(Date, nullable=False)

    gtin: str = Column(String, nullable=False)
    prid: str = Column(String, nullable=False)
    product: "Product" = relationship("Product", backref="moves", foreign_keys=[gtin, prid])

    sender_inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    sender: "Participant" = relationship("Participant", backref="sent_products", foreign_keys=[sender_inn])

    receiver_inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    receiver: "Participant" = relationship(
        "Participant",
        backref="received_products",
        foreign_keys=[receiver_inn],
    )

    cnt_moved: int = Column(Integer, nullable=False)

    __table_args__ = (ForeignKeyConstraint([gtin, prid], ["product.gtin", "product.inn"]), {})
