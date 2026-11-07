import pandas as pd

def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    orders['purchase_date']=pd.to_datetime(orders['purchase_date'])
    orders['year']=orders['purchase_date'].dt.year
    p=orders.groupby(['product_id','year'])['order_id'].count().reset_index(name='c')
    p=p[p['c']>=3]
    p['ny']=p.groupby(['product_id'])['year'].shift(-1)
    return (p[p['year']+1==p['ny']][['product_id']].drop_duplicates())
    