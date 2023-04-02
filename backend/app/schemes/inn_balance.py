from .base import CamelModel


class InnBalance(CamelModel):
    gtin: str
    inn: str
    positive_sum_cnt: int
    negative_sum_cnt: int

    class Config:
        orm_mode = True
