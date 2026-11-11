import pandas as pd

def employees_with_deductions(employees: pd.DataFrame, logs: pd.DataFrame) -> pd.DataFrame:
    logs['in_time']=pd.to_datetime(logs['in_time'])
    logs['out_time']=pd.to_datetime(logs['out_time'])
   
    logs['hr']=(logs['out_time']-logs['in_time']).dt.total_seconds() / 60
    logs['hr']=np.ceil(logs['hr'])
    employees['nh']=employees['needed_hours']*60
    m=logs.groupby(['employee_id'])['hr'].sum()
    res=employees.merge(m, on='employee_id',how='left').fillna(0)
    return res[res['nh']>res['hr']][['employee_id']]