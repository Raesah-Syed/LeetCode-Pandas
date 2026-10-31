import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date']=pd.to_datetime(orders['order_date'])
    ord2019=orders[orders['order_date'].dt.year==2019]
    m=users.merge(ord2019, left_on='user_id', right_on='buyer_id', how='left')
    x=m.groupby(['user_id','join_date'])['buyer_id'].count().reset_index()
    return (x.rename(columns={'buyer_id':'orders_in_2019','user_id':'buyer_id'}))
