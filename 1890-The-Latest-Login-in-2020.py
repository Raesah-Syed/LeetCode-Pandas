import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins['time_stamp']=pd.to_datetime(logins['time_stamp'])
    logins['year']=logins['time_stamp'].dt.year
    lo=logins[logins['year']==2020]
    m=lo.groupby(['user_id'])['time_stamp'].max().reset_index(name='last_stamp')
    return(m)
    