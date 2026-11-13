import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    c=vote.groupby(['candidateId'])['id'].count().reset_index(name='votes')
    c['rank']=c['votes'].rank(ascending=False)
    m=c.merge(candidate, left_on='candidateId', right_on='id')
    m=m[m['rank']==1]
    return (m[['name']])