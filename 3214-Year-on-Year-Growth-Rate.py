import pandas as pd

def calculate_yoy_growth(user_transactions: pd.DataFrame) -> pd.DataFrame:
    user_transactions['transaction_date']=pd.to_datetime(user_transactions['transaction_date'])
    user_transactions['year']=user_transactions['transaction_date'].dt.year
    s=user_transactions.sort_values(by=['product_id','transaction_date'])
    g=s.groupby(['product_id','year'])['spend'].sum().reset_index()
    g['prev_year']=g.groupby(['product_id'])['year'].shift(1)
    g['prev_s']=g.groupby(['product_id'])['spend'].shift(1)
    g['yoy_rate']=((g['spend']-g['prev_s'])*100.0/g['prev_s']).round(2)
    r=g.sort_values(by=['product_id','year'])
    return (r[['year','product_id','spend','prev_s','yoy_rate']].rename(columns={
        'spend':'curr_year_spend','prev_s':'prev_year_spend'
    }))