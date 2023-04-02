from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Column, String

from app.database.base import Base

if TYPE_CHECKING:
    from .product import Product
    from .product_in_turnover import ProductInTurnover
    from .product_move import ProductMove
    from .product_out_turnover import ProductOutTurnover
    from .sales_point import SalesPoint


class Participant(Base):
    """Справочник участников оборота товаров."""

    inn: str = Column(String, primary_key=True, index=True, unique=True, default=uuid4)
    region_code: str = Column(String, nullable=False)
    products: list["Product"]
    sales_points: list["SalesPoint"]
    in_turnovers: list["ProductInTurnover"]
    out_turnovers: list["ProductOutTurnover"]
    sent_products: list["ProductMove"]
    received_products: list["ProductMove"]
