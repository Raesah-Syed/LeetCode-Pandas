import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    idr = request_accepted['requester_id'].value_counts()
    ida = request_accepted['accepter_id'].value_counts()

    r1 = idr.reset_index()
    r2 = ida.reset_index()

    result = pd.concat([
        r1.rename(columns={'requester_id': 'id'}),
        r2.rename(columns={'accepter_id': 'id'})
    ])

    r = result.groupby('id', as_index=False)['count'].sum()

    s = r.sort_values('count', ascending=False)
    fin=s.iloc[[0]][['id', 'count']]
    return fin.rename(columns={'count': 'num'})
