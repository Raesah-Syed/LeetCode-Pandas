import pandas as pd

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    m=point2_d.merge(point2_d, how='cross')
    m=m[(m['x_x']!=m['x_y']) | (m['y_x']!=m['y_y'])]
    m
    m['d']= (((m['x_y']-m['x_x'])**2) + ((m['y_y']-m['y_x'])**2))**0.5
    x=m.sort_values(by='d')['d'].round(2)
    return pd.DataFrame({'shortest':[(x.iloc[0])]})