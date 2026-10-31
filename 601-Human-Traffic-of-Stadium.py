import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium=stadium[stadium['people']>=100]
    stadium['r']=stadium['id'].rank(method='first')
    stadium['g']=stadium['id']-stadium['r']
    stadium['x']=stadium.groupby(['g'])['id'].transform('count')
    return (stadium[stadium['x']>=3][['id','visit_date','people']])