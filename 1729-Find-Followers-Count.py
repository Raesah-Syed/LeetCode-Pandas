import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    res = followers.groupby('user_id')['follower_id'].count().reset_index(name='followers_count')
    return res.sort_values('user_id')