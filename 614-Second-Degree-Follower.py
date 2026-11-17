import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    m=follow.groupby(['followee'])['follower'].nunique().reset_index(name='num')
    x=follow['follower'].drop_duplicates().reset_index()
 
    m=m[m['followee'].isin(x['follower'])]
    return m.sort_values(by='followee').rename(columns={'followee':'follower'})