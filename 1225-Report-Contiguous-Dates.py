import pandas as pd

def report_contiguous_dates(failed: pd.DataFrame, succeeded: pd.DataFrame) -> pd.DataFrame:

    failed['fail_date']=pd.to_datetime(failed['fail_date'])
    succeeded['success_date']=pd.to_datetime(succeeded['success_date'])

    ff=failed[failed['fail_date'].between( '2019-01-01','2019-12-31')]
    fs=succeeded[succeeded['success_date'].between( '2019-01-01','2019-12-31')]

    sff=ff.sort_values(by='fail_date')
    sfs=fs.sort_values(by='success_date')

    sff['next_date']=sff['fail_date'].shift(-1).fillna(sff['fail_date'])
    sfs['next_date']=fs['success_date'].shift(-1).fillna(sfs['success_date'])

    sff['rank']=sff['fail_date'].rank(method='first')
    sfs['rank']=sfs['success_date'].rank(method='first')

    sff['g'] = sff['fail_date'] - pd.to_timedelta(sff['rank'], unit='D')
    sfs['g'] = sfs['success_date'] - pd.to_timedelta(sfs['rank'], unit='D')

    fd=sff[sff['fail_date']-sff['next_date']>=pd.Timedelta(days=-1)]
    sd=sfs[sfs['success_date']-sfs['next_date']>=pd.Timedelta(days=-1)]

    res1=sff.groupby(['g']).agg(
    start_date=('fail_date', 'min'),
    end_date=('fail_date', 'max')
)
    res1.insert(0,'period_state','failed')

    res2=sfs.groupby(['g']).agg(
    start_date=('success_date', 'min'),
    end_date=('success_date', 'max'))

    res2.insert(0,'period_state','succeeded')

    result=pd.concat([res1, res2], ignore_index=True)

    resu=result.sort_values(by='start_date')
    return (resu)