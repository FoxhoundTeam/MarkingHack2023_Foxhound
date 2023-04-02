from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from .participant import Participant
    from .product_out_turnover import ProductOutTurnover


class SalesPoint(Base):
    """Справочник торговых точек."""

    id_sp: str = Column(String, primary_key=True, index=True, unique=True, default=uuid4)
    inn: str = Column(String, ForeignKey("participant.inn"), nullable=False)
    participant: "Participant" = relationship("Participant", backref="sales_points")
    region_code: str = Column(String, nullable=False)
    city_with_type: str = Column(String, nullable=False)
    city_fias_id: str = Column(String, nullable=False)
    postal_code: str = Column(String, nullable=False)
    out_turnovers: list["ProductOutTurnover"]
