import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    c2=calls[['from_id','to_id','duration']].rename(columns={
        'from_id':'to_id',
        'to_id':'from_id'
    })
    x=pd.concat([calls,c2])
    x=x[x['from_id']<x['to_id']]
    return (x.groupby(['from_id','to_id']).agg(
        call_count=('duration','count'),
        total_duration=('duration','sum')).reset_index()).rename(columns={
            'from_id':'person1',
            'to_id':'person2'
        })
