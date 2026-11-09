import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    m=sales.merge(product, on='product_id')
    s8=m[m['product_name']=='S8']
    iphone=m[m['product_name']=='iPhone']
    return (s8[~s8['buyer_id'].isin(iphone['buyer_id'])][['buyer_id']].drop_duplicates())