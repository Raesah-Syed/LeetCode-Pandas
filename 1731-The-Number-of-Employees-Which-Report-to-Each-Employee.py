import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    m=employees.merge(employees, left_on='reports_to', right_on='employee_id',suffixes=('_e',''))
    m['average_age'] = (m.groupby(['employee_id', 'name'])['age_e'].transform('mean') + 1e-9).round()
    m['reports_count'] = m.groupby(['employee_id', 'name'])['employee_id_e'].transform('count')
    return m[['employee_id','name','reports_count','average_age']].drop_duplicates().sort_values(by='employee_id')