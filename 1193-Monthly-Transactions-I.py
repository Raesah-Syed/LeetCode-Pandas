import pandas as pd
import numpy as np

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["trans_date"]=transactions["trans_date"].dt.to_period('M').astype(str)
    transactions = transactions.rename(columns={'trans_date': 'month'})
    transactions["approved_count"]=np.where(transactions['state']=='approved',1,0)
    transactions["approved_amount"]=np.where(transactions['state']=='approved',transactions['amount'],0)
    gd=transactions.groupby(['month','country'],dropna=False).agg({'amount':'sum','id':'count','approved_count':'sum','approved_amount':'sum'})
    gd=gd.rename(columns={'id':'trans_count','amount':'trans_total_amount','approved_amount':'approved_total_amount'})
    return gd.reset_index()[[
        'month', 
        'country', 
        'trans_count', 
        'approved_count', 
        'trans_total_amount', 
        'approved_total_amount'
    ]]