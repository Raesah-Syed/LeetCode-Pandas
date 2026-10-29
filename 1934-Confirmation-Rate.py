import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    ccount=confirmations[confirmations['action']=='confirmed'].value_counts('user_id')
    tcount=confirmations.value_counts('user_id')
    x=ccount.reset_index(name='cc')
    y=tcount.reset_index(name='tc')
    r=x.merge(y,on='user_id')
    res=signups.merge(r,on='user_id', how='left', suffixes=('','_t')).fillna(0)
    res['confirmation_rate']=(res['cc']/res['tc']).fillna(0).round(2)
    return (res[['user_id','confirmation_rate']])
