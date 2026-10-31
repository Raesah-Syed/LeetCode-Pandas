import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    p=project.merge(employee, on='employee_id')
    p['average_years']=p.groupby(['project_id'])['experience_years'].transform('mean').round(2)
    return p[['project_id','average_years']].drop_duplicates()