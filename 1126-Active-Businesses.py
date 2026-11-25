import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    events['aa']=events.groupby(['event_type'])['occurrences'].transform('mean')
    ab=events[events['occurrences']>events['aa']]
    v=ab.groupby(['business_id'])['event_type'].nunique().reset_index(name='c')
    return (v[v['c']>1][['business_id']])