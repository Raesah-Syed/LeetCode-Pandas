import pandas as pd

def average_salary(salary: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
     salary['pay_date']=pd.to_datetime(salary['pay_date'])
     salary['pay_month']=salary['pay_date'].dt.strftime('%Y-%m')
     m=salary.merge(employee, on='employee_id')
     r=m.groupby(['pay_month','department_id'])['amount'].mean().round(2).reset_index()
     s=m.groupby(['pay_month'])['amount'].mean().round(2)
     res=r.merge(s, on='pay_month')
     res['comparison']=np.where(res['amount_x']>res['amount_y'],'higher','lower')
     res['comparison']=np.where(res['amount_x']==res['amount_y'],'same',res['comparison'])
     return (res[['pay_month','department_id','comparison']])