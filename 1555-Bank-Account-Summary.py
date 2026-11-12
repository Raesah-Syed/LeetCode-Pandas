import pandas as pd

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    paid=transactions.groupby(['paid_by'])['amount'].sum()
    rec=transactions.groupby(['paid_to'])['amount'].sum()

    users['paid']=users['user_id'].map(paid).fillna(0)
    users['rec']=users['user_id'].map(rec).fillna(0)

    users['credit']=users['credit']-users['paid']+users['rec']
    users['credit_limit_breached']= users['credit'].apply(lambda x: 'Yes' if x<0 else 'No')

    return (users[['user_id','user_name','credit','credit_limit_breached']])