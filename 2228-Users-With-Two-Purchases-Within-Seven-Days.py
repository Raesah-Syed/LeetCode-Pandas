import pandas as pd

def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:
    purchases['purchase_date']=pd.to_datetime(purchases['purchase_date'])
    purchases=purchases.sort_values(by=['user_id','purchase_date'])
    purchases['nd']=purchases.groupby(['user_id'])['purchase_date'].shift(-1)
    purchases['d']=purchases['nd']-purchases['purchase_date']
    purchases=purchases[purchases['d'].between('0 days','7 days')]
    return (purchases[['user_id']].sort_values(by='user_id').drop_duplicates())