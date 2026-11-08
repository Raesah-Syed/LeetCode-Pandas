import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    s=sales.groupby(['seller_id'])['price'].sum().reset_index()
    s['max']=s['price'].max()
    return (s[s['price']==s['max']][['seller_id']])