import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    m=project.merge(employee, on ='employee_id')
    m['exp']=m.groupby(['project_id'])['experience_years'].rank(method='dense', ascending=False)
    return (m[m['exp']==1][['project_id','employee_id']])