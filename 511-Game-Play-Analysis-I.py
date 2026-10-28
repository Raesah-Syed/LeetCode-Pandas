import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    res=activity.groupby(activity['player_id'])['event_date'].min()
    
    return (res.reset_index(name='first_login'))