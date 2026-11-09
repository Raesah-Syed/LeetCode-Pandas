import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    c=championships.melt(
        id_vars='year',
        var_name='match',
        value_name='player_id').reset_index()
    m=c.groupby(['player_id'])['match'].count().reset_index(name='grand_slams_count')
    r=m.merge(players, on='player_id', suffixes=('','_y'))
    return (r[['player_id','player_name','grand_slams_count']])