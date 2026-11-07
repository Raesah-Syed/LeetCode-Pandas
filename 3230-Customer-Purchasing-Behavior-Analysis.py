import pandas as pd

def analyze_customer_behavior(transactions: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    transactions['transaction_date']=pd.to_datetime(transactions['transaction_date'])
    t=transactions.merge(products, on='product_id')
    
    x=t.sort_values(by=['customer_id','transaction_date'],ascending=[True,False])
    x['c']=x.groupby(['customer_id','category'])['transaction_id'].transform('nunique')
    s=x.sort_values(by=['customer_id','c'], ascending=[True,False])

    r=(s[['customer_id','category']].drop_duplicates(subset=['customer_id'],keep='first'))
    t=t.groupby(['customer_id']).agg(
        total_amount=('amount','sum'),
        transaction_count=('transaction_id','count'),
        unique_categories=('category','nunique'),
        avg_transaction_amount=('amount','mean'),
    ).reset_index()
  
    t['loyalty_score']=(t['transaction_count']*10)+(t['total_amount']/100.0)
    res=t.merge(r, on='customer_id')
    cols = ['total_amount','avg_transaction_amount','loyalty_score']
    res[cols] = (res[cols] + 1e-9).round(2)
    return (res[['customer_id','total_amount','transaction_count','unique_categories','avg_transaction_amount','category','loyalty_score']].rename(columns={'category':'top_category'})).sort_values(by=['loyalty_score','customer_id'], ascending=[False,True])
    