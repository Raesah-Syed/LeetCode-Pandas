import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    actions['action_date']=pd.to_datetime(actions['action_date'])
    actions=actions[(actions['action']=='report') & (actions['action_date']=='2019-07-04')]
    res=actions.groupby(['extra'])['post_id'].nunique().reset_index(name='report_count')
    return (res.rename(columns={'extra':'report_reason'}))