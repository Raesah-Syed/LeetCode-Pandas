import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity=activity.sort_values(by='event_date')
    activity['games_played_so_far']=activity.groupby(['player_id'])['games_played'].cumsum()
    return activity[['player_id','event_date','games_played_so_far']]