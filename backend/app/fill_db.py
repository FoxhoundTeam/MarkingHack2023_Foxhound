import pandas as pd

from app.database import (
    Base,
    Participant,
    Product,
    ProductInTurnover,
    ProductMove,
    ProductOutTurnover,
    SalesPoint,
    SessionLocal,
)


def _get_df(df: str | pd.DataFrame):
    if isinstance(df, str):
        df = pd.read_csv(df, index_col=0)
    return df


def _fill_from_df(df: pd.DataFrame, model_cls: type[Base]):
    with SessionLocal() as session:
        session.add_all([model_cls(**row) for row in df.to_dict("records")])
        session.commit()


def fill_participants(filename: str):
    _fill_from_df(_get_df(filename), Participant)


def fill_products(filename: str):
    _fill_from_df(_get_df(filename), Product)


def fill_sales_points(filename: str):
    _fill_from_df(_get_df(filename), SalesPoint)


def fill_product_in_turnovers(filename: str):
    _fill_from_df(_get_df(filename), ProductInTurnover)


def fill_product_moves(filename: str):
    _fill_from_df(_get_df(filename), ProductMove)


def fill_product_out_turnovers(filename: str):
    _fill_from_df(_get_df(filename), ProductOutTurnover)
