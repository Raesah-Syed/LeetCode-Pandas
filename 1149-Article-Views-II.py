import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
#group by view_date and viewer_id
    x=views.groupby(['view_date','viewer_id'])['article_id'].nunique().reset_index(name='views')
    res=x[x['views']>1][['viewer_id']]
    return (res.sort_values(by='viewer_id').drop_duplicates().rename(columns={'viewer_id':'id'}))