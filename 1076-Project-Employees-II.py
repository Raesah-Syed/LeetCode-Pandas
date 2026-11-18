import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    m=project.groupby(['project_id'])['employee_id'].count().reset_index(name='cnt')
    m['rank']=m['cnt'].rank(method='dense', ascending=False)
    return pd.DataFrame({'project_id':m[m['rank']==1]['project_id']})