import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    m=point.merge(point, how='cross')
    m=m[(m['x_x']!=m['x_y']) & (m['x_x']<m['x_y'])]
    m['shortest']=np.abs(m['x_x']-m['x_y'])
    return pd.DataFrame({'shortest':[m.sort_values(by='shortest').iloc[0]['shortest']]})
