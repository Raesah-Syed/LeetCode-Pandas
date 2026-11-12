import pandas as pd

def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:
    steps['steps_date']=pd.to_datetime(steps['steps_date'])

    steps=steps.sort_values(by=['user_id','steps_date'])    
    steps['rolling_average'] = steps.groupby('user_id')['steps_count'].rolling(3).mean().values.round(2)
    steps['p1']=steps.groupby(['user_id'])['steps_date'].shift(1)
    steps['p2']=steps.groupby(['user_id'])['steps_date'].shift(2)

    res=steps[(steps['steps_date']-steps['p1']==pd.Timedelta(days=1)) & (steps['steps_date']-steps['p2']==pd.Timedelta(days=2))]

    return (res[['user_id','steps_date','rolling_average']])