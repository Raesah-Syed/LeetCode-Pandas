import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    orders['rank']=orders.groupby('product_id')['order_date'].rank(ascending=False, method='dense')
    order=orders[orders['rank']==1]
    res=order.merge(products, on='product_id')
    return (res.sort_values(by=['product_name','product_id','order_id'])[['product_name','product_id','order_id','order_date']])