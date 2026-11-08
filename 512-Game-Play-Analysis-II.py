import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date']=pd.to_datetime(activity['event_date'])
    activity['m']=activity.groupby(['player_id'])['event_date'].transform('min')
    return (activity[activity['m']==activity['event_date']][['player_id','device_id']])