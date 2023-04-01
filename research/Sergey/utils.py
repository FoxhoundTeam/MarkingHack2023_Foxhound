import pandas as pd

def calc_region_price_product(df_out, df_participations, gtin=None, region_code=None):
    """Calculation of the market price for this product by region
    
    Args:
    * df_out: df: data on the withdrawal of goods from circulation.
    * df_participations: df: directory of product turnover participants.
    * gtin: list or tuple or series of strings: if None return all.
    * region_code: list or tuple or series of floats: if None return all.
    
    Return:
    * DataFrame with columns: gtin, region_code, price (median, mean, min, max, count).
    """
    if region_code is not None:
        df_participations = df_participations[df_participations.region_code.isin(region_code)]
    if gtin is not None:
        df = df_out.loc[df_out.gtin.isin(gtin), ("gtin", "price", "inn")]
    else:
        df = df_out[["gtin", "price", "inn"]]
    df = df.merge(df_participations, how="left")\
        [df_out.type_operation != "Списание / Вывод из оборота без получателя"]
    df_price_reg = df[["gtin", "price", "region_code"]]
    return df_price_reg.groupby(["gtin", "region_code"]).agg({
        "price": ["median", "mean", "min", "max", "count"]
    })