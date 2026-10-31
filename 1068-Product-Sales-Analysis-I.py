import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    m=sales.merge(product, on='product_id')
    return (m[['product_name','year','price']])