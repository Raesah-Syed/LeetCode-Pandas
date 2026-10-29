import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    x=employee.groupby(['departmentId'])['salary'].max().reset_index()
    r=employee.merge(x, on=['departmentId','salary'])
    res=r.merge(department, left_on='departmentId',right_on='id', suffixes=('','_y'))
    return res[['name_y','name','salary']].rename(columns={'name_y':'Department','name':'Employee','salary':'Salary'})