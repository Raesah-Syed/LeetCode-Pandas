import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_date']=pd.to_datetime(orders['order_date'])
    o=orders[orders['order_date'].between('2020-02-01','2020-02-29')]
    c=o.groupby(['product_id'])['unit'].sum().reset_index()
    m=c[c['unit']>=100].merge(products, on='product_id')
    return (m[['product_name','unit']])
