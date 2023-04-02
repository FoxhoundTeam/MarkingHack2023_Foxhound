from uuid import uuid4

from sqlalchemy import Column, String

from app.database.base import Base


class SalesPoint(Base):
    """Справочник торговых точек."""

    id_sp: str = Column(String, primary_key=True, index=True, unique=True, default=uuid4)
    inn: str = Column(String, nullable=False, index=True)
    region_code: str = Column(String, nullable=False)
    city_with_type: str = Column(String, nullable=False)
    city_fias_id: str = Column(String, nullable=False)
    postal_code: str = Column(String, nullable=False)
