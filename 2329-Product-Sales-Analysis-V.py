import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    m=sales.merge(product, on='product_id', how='left')
    m['spending']=m['quantity']*m['price']
    res=m.groupby(['user_id'])['spending'].sum().reset_index()
    return res.sort_values(by=['spending','user_id'], ascending=[False, True])[['user_id','spending']]