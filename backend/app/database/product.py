from sqlalchemy import Column, String

from app.database.base import Base


class Product(Base):
    """Справочник продукции."""

    gtin: str = Column(String, nullable=False, primary_key=True, index=True)
    inn: str = Column(String, nullable=False, primary_key=True, index=True)
    product_name: str = Column(String, nullable=False)
    product_short_name: str = Column(String, nullable=False)
    tnved: str = Column(String, nullable=False)
    tnved10: str = Column(String, nullable=False)
    brand: str = Column(String, nullable=False)
    country: str = Column(String, nullable=False)
    volume: str = Column(String, nullable=False)
