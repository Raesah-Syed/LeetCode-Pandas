import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager=employee
    r=employee.merge(manager, left_on="managerId", right_on="id", suffixes=('','_manager'))
    filtered=r[r['salary']>r['salary_manager']]
    return filtered[['name']].rename(columns={'name': 'Employee'})