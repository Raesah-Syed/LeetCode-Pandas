import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    d = activity[(activity['activity_date'] <= pd.to_datetime('2019-07-27')) & (activity['activity_date'] >= pd.to_datetime('2019-07-27') - pd.Timedelta(days=29))]
    return (d.groupby('activity_date')['user_id'].nunique().reset_index().rename(columns={'activity_date':'day','user_id':'active_users'}))