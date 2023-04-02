from typing import TYPE_CHECKING

from sqlalchemy import func, select

from app.database import ProductInTurnover, ProductOutTurnover
from app.services.base import BaseDBService

if TYPE_CHECKING:
    from datetime import date

    from app.schemes import OnMarket


class OnMarketService(BaseDBService):
    def _get_query(self, dt: "date"):
        return (
            select(
                (func.sum(ProductInTurnover.cnt) - func.sum(ProductOutTurnover.cnt)).label("cnt"),
                ProductInTurnover.gtin,
            )
            .join_from(
                ProductInTurnover,
                ProductOutTurnover,
                (ProductInTurnover.gtin == ProductOutTurnover.gtin),
            )
            .where(ProductInTurnover.dt <= dt, ProductOutTurnover.dt <= dt)
            .group_by(ProductInTurnover.gtin)
        )

    def get_all(self, dt: "date") -> list["OnMarket"]:
        return self.session.execute(self._get_query(dt)).scalars().all()

    def get(self, gtin: str, dt: "date") -> "OnMarket":
        return self.session.execute(self._get_query(dt).where(ProductInTurnover.gtin == gtin)).first()
