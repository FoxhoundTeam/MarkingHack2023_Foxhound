from .base import CamelModel


class OnMarket(CamelModel):
    gtin: str
    cnt: int

    class Config:
        orm_mode = True
