import pandas as pd

def find_longest_calls(contacts: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    calls['rank']=calls.groupby(['type'])['duration'].rank(method='first',ascending=False)
    v=calls[calls['rank']<=3]
    v['hour'] = (v['duration'] // 3600).astype(str).str.zfill(2)
    v['min'] = ((v['duration'] % 3600) // 60).astype(str).str.zfill(2)
    v['sec'] = (v['duration'] % 60).astype(str).str.zfill(2)
    v['duration_formatted'] = v[['hour','min','sec']].astype(str).agg(":".join, axis=1)
    m=v.merge(contacts, left_on='contact_id',right_on='id')
    return (m.sort_values(by=['type','duration','first_name'], ascending=[False,False,False])[['first_name','type','duration_formatted']])