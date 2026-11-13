import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    sl=survey_log[survey_log['action']!='skip']
    sl['show']=numpy.where(sl['action']=='show',1,0)
    sl['answer']=numpy.where(sl['action']=='answer',1,0)
    r=sl.groupby(['question_id']).agg(
        sh=('show','sum'),an=('answer','sum')
    ).reset_index()
    r['rate']=r['an']*1.0/r['sh']
    r['rank']=r['rate'].rank(method='first',ascending=False)
    res=r[r['rank']==1]
    return res[['question_id']].rename(columns={'question_id':'survey_log'})
