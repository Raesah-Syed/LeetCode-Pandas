import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    m=employees.merge(employee_uni, on='id', how='left', suffixes=('','_y'))
    return (m[['unique_id','name']])
    