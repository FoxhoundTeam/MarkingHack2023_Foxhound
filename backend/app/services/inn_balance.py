from datetime import date

from sqlalchemy import func, select

from app.database import ProductInTurnover, ProductMove, ProductOutTurnover
from app.schemes import InnBalance

from .base import BaseDBService


class InnBalanceService(BaseDBService):
    def _get_query(self, dt: date):
        return (
            select(
                ProductInTurnover.gtin,
                ProductInTurnover.inn,
                (
                    func.sum(ProductInTurnover.cnt)
                    + func.sum(ProductMove.cnt_moved).filter(ProductMove.receiver_inn == ProductInTurnover.inn)
                ).label("positive_sum_cnt"),
                (
                    func.sum(ProductOutTurnover.cnt)
                    + func.sum(ProductMove.cnt_moved).filter(ProductMove.sender_inn == ProductInTurnover.inn)
                ).label("negative_sum_cnt"),
            )
            .join(
                ProductMove,
                (ProductInTurnover.gtin == ProductMove.gtin)
                & (
                    (ProductInTurnover.inn == ProductMove.sender_inn)
                    | (ProductInTurnover.inn == ProductMove.receiver_inn)
                ),
            )
            .join(
                ProductOutTurnover,
                (ProductInTurnover.gtin == ProductOutTurnover.gtin) & (ProductInTurnover.inn == ProductOutTurnover.inn),
            )
            .where(ProductInTurnover.dt <= dt, ProductOutTurnover.dt <= dt, ProductMove.dt <= dt)
            .group_by(ProductInTurnover.gtin, ProductInTurnover.inn)
        )

    def get_all(self, dt: "date") -> list["InnBalance"]:
        return self.session.execute(self._get_query(dt)).scalars().all()

    def get(self, gtin: str, inn: str, dt: "date") -> "InnBalance":
        return self.session.execute(
            self._get_query(dt).where(
                ProductInTurnover.gtin == gtin,
                ProductInTurnover.inn == inn,
            ),
        ).first()
