import pandas as pd

def longest_winning_streak(matches: pd.DataFrame) -> pd.DataFrame:
    matches['s']=matches.groupby(['player_id'])['match_day'].rank(method='first')
    matches['w']=matches.groupby(['player_id','result'])['match_day'].rank(method='first')
    matches['g']=matches['s']-matches['w']
    match=matches[matches['result']=='Win']
    g=match.groupby(['player_id','g'])['match_day'].count().reset_index(name='longest_streak')
    ls=g.groupby(['player_id'])['longest_streak'].max().reset_index()
    res=matches['player_id'].drop_duplicates().reset_index().merge(ls, on='player_id', how='left')
    return (res.fillna(0)[['player_id','longest_streak']])
    