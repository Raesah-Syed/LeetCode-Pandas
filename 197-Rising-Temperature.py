import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate']=pd.to_datetime(weather['recordDate'])
    m=weather.merge(weather, how="cross",suffixes=('','_y'))
    n= m[(m['recordDate']-m['recordDate_y'])==pd.Timedelta(days=1)]
    f=n[n['temperature']>n['temperature_y']]
    return f[['id']]