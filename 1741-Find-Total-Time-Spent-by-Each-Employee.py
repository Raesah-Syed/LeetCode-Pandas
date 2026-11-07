import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time']=employees['out_time']-employees['in_time']
    x=employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index()
    return (x.rename(columns={'event_day':'day'}))