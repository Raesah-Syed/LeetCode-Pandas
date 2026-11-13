import pandas as pd

def median_frequency(numbers: pd.DataFrame) -> pd.DataFrame:
    numbers=numbers.sort_values(by='num')
    numbers['end']=numbers['frequency'].cumsum()
    numbers['start']=numbers['end']-numbers['frequency']
    numbers['tot']=numbers['frequency'].sum()
    numbers['mid']=numbers['tot']/2
    num=numbers[numbers['mid'].between(numbers['start'],numbers['end'])].drop_duplicates()
    num['median']= (num['num'].mean())
    return pd.DataFrame(num['median']).drop_duplicates()