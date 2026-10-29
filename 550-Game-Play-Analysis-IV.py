import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    s = activity.sort_values(['player_id', 'event_date'])
    s['event_date'] = pd.to_datetime(s['event_date'])
    s['prev'] = s.groupby('player_id')['event_date'].shift(1)
    tot = s['player_id'].nunique()
    x = s[(s['event_date'] - s['prev'] == pd.Timedelta(days=1)) &
          (s['prev'] == s.groupby('player_id')['event_date'].transform('min'))]
    xs = x['player_id'].nunique()
    return pd.DataFrame({'fraction': [round(xs / tot, 2)]})