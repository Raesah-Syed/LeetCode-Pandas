import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    tr=transactions['visit_id'].drop_duplicates()
    ex=visits[~visits['visit_id'].isin(tr)]
    res=ex['customer_id'].value_counts().reset_index()
    return res.rename(columns={'count':'count_no_trans'})