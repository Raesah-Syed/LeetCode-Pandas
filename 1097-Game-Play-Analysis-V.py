import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date']=pd.to_datetime(activity['event_date'])
    activity=activity.sort_values(by=['player_id', 'event_date'])
    activity['r']=activity.groupby('player_id')['event_date'].rank()
    rel=activity[activity['r']<=2]
    num=rel[rel['r']==1].groupby('event_date')['player_id'].count().reset_index(name='installs')
    rel['nd']=rel.groupby('player_id')['event_date'].shift(-1)
    den=rel[rel['nd']-rel['event_date']==pd.Timedelta(days=1)]
    nume=den.groupby('event_date')['player_id'].count().reset_index(name='n')
    res=num.merge(nume, on='event_date', how='left')
    res['Day1_retention']=np.where(res['n'].isna(),0.0,((res['n']+1e-9)*1.0/res['installs']).round(2))
    return (res[['event_date','installs','Day1_retention']].rename(columns={'event_date':'install_dt'}))
