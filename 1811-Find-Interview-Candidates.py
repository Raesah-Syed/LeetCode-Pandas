import pandas as pd

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    x=contests.melt(
        id_vars='contest_id',
        var_name='medal',
        value_name='user_id'
    )
    x['tr']=x.groupby(['user_id'])['contest_id'].rank(method='first')
    x['g']=x['contest_id']-x['tr']
    y=x.groupby(['user_id','g'])['contest_id'].count().reset_index(name='cc')
    any_medals=y[y['cc']>=3][['user_id']].drop_duplicates()
    
    g=x[x['medal']=='gold_medal'].groupby(['user_id'])['contest_id'].count().reset_index(name='cnt')
    m3=g[g['cnt']>=3]

    d=pd.concat([any_medals['user_id'],m3['user_id']]).reset_index()
    
    return (users[users['user_id'].isin(d['user_id'])][['name','mail']])