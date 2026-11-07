import pandas as pd
import numpy

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    c=customer_transactions[customer_transactions['transaction_type']=='purchase']
    cc=c.groupby(['customer_id'])['transaction_id'].nunique().reset_index()
    vc=cc[cc['transaction_id']>=3]
    customer_transactions['transaction_date']=pd.to_datetime(customer_transactions['transaction_date'])
    mm=customer_transactions.groupby(['customer_id']).agg(first=('transaction_date','min'), last=('transaction_date','max')).reset_index()
    vm=mm[mm['last']-mm['first']>=pd.Timedelta(30,unit='D')]
    customer_transactions['ref']=numpy.where(customer_transactions['transaction_type']=='refund',1,0)
    rr=customer_transactions.groupby(['customer_id']).agg(ref=('ref','sum'),tot=('transaction_id','nunique')).reset_index()
    rr['rp']=((rr['ref']*100)/rr['tot']).round(2)
    rr=rr[rr['rp']<20]
    v = set(vc['customer_id']) & set(vm['customer_id']) & set(rr['customer_id'])
    return customer_transactions[customer_transactions['customer_id'].isin(v)][['customer_id']].drop_duplicates().reset_index(drop=True)