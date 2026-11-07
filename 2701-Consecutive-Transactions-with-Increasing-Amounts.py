import pandas as pd

def consecutive_increasing_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['transaction_date']=pd.to_datetime(transactions['transaction_date'])
    transactions = transactions.sort_values(['customer_id', 'transaction_date'])
    transactions['nd']=transactions.groupby(['customer_id'])['transaction_date'].shift(-1)
    transactions['na']=transactions.groupby(['customer_id'])['amount'].shift(-1)

    vt=transactions[(transactions['nd']-transactions['transaction_date']=='1 days') & (transactions['na']>transactions['amount'])]
    
    vt['rank']=vt.groupby(['customer_id'])['transaction_date'].rank()
    vt['g']=vt['transaction_date']- pd.to_timedelta(vt['rank'], unit='D')
    
    r=vt.groupby(['customer_id','g']).agg(
        t=('transaction_id','nunique'),
        consecutive_start=('transaction_date','min'),
        consecutive_end=('nd','max')
    )

    return (r[r['t']>=2].reset_index()[['customer_id','consecutive_start','consecutive_end']])