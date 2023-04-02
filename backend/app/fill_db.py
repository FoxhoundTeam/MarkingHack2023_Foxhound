import pandas as pd
from sqlalchemy import select

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


participants_query = select(Participant.inn)


def fill_sales_points(filename: str):
    df = _get_df(filename)
    with SessionLocal() as session:
        participants_from_db = session.execute(participants_query).scalars().all()
    df = df[df["inn"].isin(participants_from_db)]
    _fill_from_df(df, SalesPoint)


products_query = select(Product.inn, Product.gtin)


def fill_product_in_turnovers(filename: str):
    df = _get_df(filename)

    with SessionLocal() as session:
        participants_from_db = session.execute(participants_query).scalars().all()
        products_from_db = session.execute(products_query).all()

    df = df[(df["inn"].isin(participants_from_db)) & df.set_index(["prid", "gtin"]).index.isin(products_from_db)]

    _fill_from_df(df, ProductInTurnover)


def fill_product_moves(filename: str):
    df = _get_df(filename)

    with SessionLocal() as session:
        participants_from_db = session.execute(participants_query).scalars().all()
        products_from_db = session.execute(products_query).all()

    df = df[
        (df["sender_inn"].isin(participants_from_db))
        & df.set_index(["prid", "gtin"]).index.isin(products_from_db)
        & (df["receiver_inn"].isin(participants_from_db))
    ]

    _fill_from_df(df, ProductMove)


def fill_product_out_turnovers(filename: str):
    df = _get_df(filename)

    sales_point_query = select(SalesPoint.id_sp)

    with SessionLocal() as session:
        participants_from_db = session.execute(participants_query).scalars().all()
        products_from_db = session.execute(products_query).all()
        sales_points_from_db = session.execute(sales_point_query).scalars().all()

    df = df[
        (df["inn"].isin(participants_from_db))
        & df.set_index(["prid", "gtin"]).index.isin(products_from_db)
        & (df["id_sp"].isin(sales_points_from_db))
    ]

    _fill_from_df(df, ProductOutTurnover)
