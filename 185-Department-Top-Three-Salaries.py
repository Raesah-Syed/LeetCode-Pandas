import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank']=employee.groupby(['departmentId'])['salary'].rank(ascending=False,method='dense')
    f=employee[employee['rank']<=3][['name','salary','departmentId']]
    m=f.merge(department,left_on='departmentId', right_on='id', suffixes=('','_d'))
    return (m[['name_d','name','salary']].rename(columns={'name':'Employee','salary':'Salary','name_d':'Department'}))
  
