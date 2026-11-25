import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity['activity_date']=pd.to_datetime(activity['activity_date'])
    activity['pr']=pd.to_datetime('2019-07-27')-pd.Timedelta(days=29)
    act=activity[(activity['activity_date']>=activity['pr']) & (activity['activity_date']<=pd.to_datetime('2019-07-27'))]
    g=act.groupby(['user_id'])['session_id'].nunique().reset_index(name='c')
    r=((g['c'].sum()*1.0)/g['c'].count()).round(2)
    return pd.DataFrame({'average_sessions_per_user':[0 if pd.isna(r) else r]})