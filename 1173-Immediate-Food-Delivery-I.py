import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['i']=np.where(delivery['order_date']==delivery['customer_pref_delivery_date'],1,0)
    res=((delivery['i'].sum())*100.0/delivery['i'].count()).round(2)
    return pd.DataFrame({'immediate_percentage':[res]})