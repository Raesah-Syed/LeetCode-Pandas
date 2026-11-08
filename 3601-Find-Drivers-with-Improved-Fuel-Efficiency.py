import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['trip_date']=pd.to_datetime(trips['trip_date'])
    fh=trips[trips['trip_date'].dt.month.between(1,6)]
    lh=trips[trips['trip_date'].dt.month.between(7,12)]
    fh['fe']=fh['distance_km']/fh['fuel_consumed']
    first=fh.groupby(['driver_id'])['fe'].mean().reset_index(name='first_half_avg')
    lh['fe']=lh['distance_km']/lh['fuel_consumed']
    last=lh.groupby(['driver_id'])['fe'].mean().reset_index(name='second_half_avg')
    m=first.merge(last, on='driver_id')
    res=m.merge(drivers, on='driver_id')
    res['efficiency_improvement']=(res['second_half_avg']-res['first_half_avg'])
    result=res[['driver_id','driver_name','first_half_avg','second_half_avg','efficiency_improvement']].round(2).sort_values(by=['efficiency_improvement','driver_name'], ascending=[False, True]).reset_index(drop=True)
    t=result[result['efficiency_improvement']>0]
    return t

