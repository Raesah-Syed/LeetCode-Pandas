import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    x = orders.groupby(['customer_id','product_id'])['order_id'].count().reset_index(name='c')
    y=x.groupby(['customer_id'])['c'].max().reset_index()
    res=x.merge(y, on=['customer_id','c']).reset_index()[['customer_id','product_id']]
    r=res.merge(products, on='product_id').reset_index()
    return (r[['customer_id','product_id','product_name']])