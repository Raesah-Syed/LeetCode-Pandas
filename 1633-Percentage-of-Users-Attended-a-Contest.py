import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    cf=register.groupby(['contest_id'])['user_id'].count().reset_index()
    u=sum(users['user_id'].value_counts())
    cf['percentage']=((cf['user_id']*100.0)/u).round(2)
    return cf.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])[['contest_id', 'percentage']]