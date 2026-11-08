import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    employee['team_size']=employee.groupby(['team_id'])['employee_id'].transform('nunique')
    return employee[['employee_id','team_size']]