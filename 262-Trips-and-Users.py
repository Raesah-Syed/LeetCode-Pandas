import pandas as pd
import numpy as np

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    x = users[users['banned'] == 'No'][['users_id']]
    trips['request_at']=pd.to_datetime(trips['request_at'])
    ut = trips[
        trips['client_id'].isin(x['users_id']) &
        trips['driver_id'].isin(x['users_id']) & trips['request_at'].between('2013-10-01','2013-10-03')
    ].copy()

    ut['c'] = np.where(ut['status'] != 'completed', 1, 0)
    ut['t'] = ut.groupby('request_at')['id'].transform('count')

    s = ut.groupby('request_at').agg(
        n=('c', 'sum'),
        d=('id', 'count')
    ).reset_index()

    s['Cancellation Rate'] = (s['n'] / s['d']).round(2)

    return s[['request_at', 'Cancellation Rate']].rename(
        columns={'request_at': 'Day'}
    )