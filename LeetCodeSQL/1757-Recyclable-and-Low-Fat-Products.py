import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    r=products[(products["low_fats"]=='Y') & (products["recyclable"]=='Y')]
    return r[["product_id"]]