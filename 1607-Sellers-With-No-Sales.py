import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    orders['sale_date']=pd.to_datetime(orders['sale_date']).dt.year
    sell=orders[orders['sale_date']==2020][['seller_id']].drop_duplicates()
    m=seller[~seller['seller_id'].isin(sell['seller_id'])]
    return (m[['seller_name']].sort_values(by='seller_name'))
    