import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    m=playback.merge(ads, on='customer_id', how='left')
    e=m[m['timestamp'].between(m['start_time'],m['end_time'])][['session_id']].drop_duplicates()
    p=m[['session_id']].drop_duplicates()
    res=p[~p['session_id'].isin(e['session_id'])]
    return (res) 
   
