import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    m=sales.merge(product, on='product_id')
    m['t']=m['price']*m['quantity']
    x=m.groupby(['user_id','product_id'])['t'].sum().reset_index()
    x['r']=x.groupby('user_id')['t'].rank(method='dense', ascending=False)
    return (x[x['r']==1][['user_id','product_id']])