import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    c=content[(content['Kids_content']=='Y') & (content['content_type']=='Movies')]
    tv_program['program_date']=pd.to_datetime(tv_program['program_date'])
    p=tv_program[tv_program['program_date'].between('2020-06-01','2020-07-01')]
    c['content_id']=c['content_id'].astype('int64')
    return (p.merge(c, on='content_id')[['title']].drop_duplicates())