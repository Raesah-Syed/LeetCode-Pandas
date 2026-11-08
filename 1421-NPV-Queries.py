import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    q=queries.merge(npv, on=['id','year'], how='left')
    return (q.fillna(0))