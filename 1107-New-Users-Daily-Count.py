import pandas as pd

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    traffic['activity_date']=pd.to_datetime(traffic['activity_date'])
    traffic=traffic[traffic['activity']=='login']

    traffic=traffic.sort_values(by=['user_id','activity_date'])
    traffic['min']=traffic.groupby(['user_id'])['activity_date'].rank(method='first')

    traffic['valid']=pd.to_datetime('2019-06-30')-pd.Timedelta(days=90)
    r=traffic[(traffic['activity_date']>=traffic['valid']) & (traffic['activity_date']<=pd.to_datetime('2019-06-30')) & (traffic['min']==1)]
    traffic=traffic.drop_duplicates()
    res=r.groupby(['activity_date'])['user_id'].count().reset_index(name='user_count')
    return (res.rename(columns={'activity_date':'login_date'}))