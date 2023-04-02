from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from .participant import Participant
    from .product_in_turnover import ProductInTurnover
    from .product_move import ProductMove
    from .product_out_turnover import ProductOutTurnover


class Product(Base):
    """Справочник продукции."""

    gtin: str = Column(String, primary_key=True, index=True, default=uuid4)
    inn: str = Column(
        String,
        ForeignKey("participant.inn"),
        nullable=False,
        primary_key=True,
        index=True,
    )
    participant: "Participant" = relationship("Participant", backref="products")
    product_name: str = Column(String, nullable=False)
    product_short_name: str = Column(String, nullable=False)
    tnved: str = Column(String, nullable=False)
    tnved10: str = Column(String, nullable=False)
    brand: str = Column(String, nullable=False)
    country: str = Column(String, nullable=False)
    volume: str = Column(String, nullable=False)
    in_turnovers: list["ProductInTurnover"]
    out_turnovers: list["ProductOutTurnover"]
    moves: list["ProductMove"]
