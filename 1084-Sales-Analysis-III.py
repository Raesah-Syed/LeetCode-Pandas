import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['sale_date']=pd.to_datetime(sales['sale_date'])
    fq=sales[sales['sale_date'].between('2019-01-01','2019-03-31')]['product_id'].reset_index()
    nq=sales[~sales['sale_date'].between('2019-01-01','2019-03-31')]['product_id'].reset_index()
    res=fq[~fq['product_id'].isin(nq['product_id'])].merge(product, on='product_id')
    return res[['product_id','product_name']].drop_duplicates()
    