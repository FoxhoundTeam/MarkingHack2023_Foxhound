from datetime import date

from sqlalchemy import between, func, select

from app.database import Product, ProductInTurnover

from .base import BaseDBService


class ImportVsLocalService(BaseDBService):
    def _get_query(self, dt_from: date, dt_to: date, group_by=Product.tnved):
        return (
            select(
                func.sum(ProductInTurnover.cnt).filter(Product.country == "РОССИЯ").label("rf"),
                func.sum(ProductInTurnover.cnt)
                .filter(Product.country in ["АРМЕНИЯ", "БЕЛАРУСЬ", "КАЗАХСТАН"])
                .label("eas"),
                func.sum(ProductInTurnover.cnt)
                .filter(Product.country not in ["РОССИЯ", "АРМЕНИЯ", "БЕЛАРУСЬ", "КАЗАХСТАН"])
                .label("foreign"),
                group_by,
            )
            .join_from(ProductInTurnover, Product, ProductInTurnover.gtin == Product.gtin)
            .where(between(ProductInTurnover.dt, dt_from, dt_to))
            .group_by(group_by)
        )

    def get_all(self, dt_from: date, dt_to: date):
        return self.session.execute(self._get_query(dt_from, dt_to)).scalars().all()

    def get(self, dt_from: date, dt_to: date, tnved: str | None = None, tnved10: str | None = None):
        group_by = Product.tnved
        value = tnved
        if value is None:
            group_by = Product.tnved10
            value = tnved10
        if value is None:
            raise ValueError

        return self.session.execute(self._get_query(dt_from, dt_to, group_by).where(group_by == value)).first()
