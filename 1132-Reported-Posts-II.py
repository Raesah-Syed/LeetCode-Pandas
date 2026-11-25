import pandas as pd

def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    spam = actions[actions['extra'] == 'spam'][['post_id','action_date']].drop_duplicates()

    res = spam.merge(removals, on='post_id', how='left')
    res['rm'] = res['remove_date'].notna().astype(int)

    r = res.groupby('action_date').agg(
        rem=('rm', 'sum'),
        tot=('post_id', 'count')
    )

    return pd.DataFrame({
        'average_daily_percent': [round((r['rem'] / r['tot'] * 100).mean(), 2)]
    })