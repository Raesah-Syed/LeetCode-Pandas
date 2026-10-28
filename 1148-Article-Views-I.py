import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    r=views[views['viewer_id']==views['author_id']][['viewer_id']]
    return (r.drop_duplicates().rename(columns={'viewer_id':'id'}).sort_values(by='id'))