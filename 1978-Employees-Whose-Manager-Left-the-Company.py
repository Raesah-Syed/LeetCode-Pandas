import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    x = employees[employees['salary'] < 30000]
    m = x.merge(
        employees,
        left_on='manager_id',
        right_on='employee_id',
        suffixes=('', '_m'),
        how='left'
    )
    return m[
        m['employee_id_m'].isna() & m['manager_id'].notna()
    ][['employee_id']].sort_values(by='employee_id')