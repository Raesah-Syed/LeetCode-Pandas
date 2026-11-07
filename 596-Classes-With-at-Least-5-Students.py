import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    x=courses.groupby(['class'])['student'].count().reset_index()
    return(pd.DataFrame({'class': x[x['student']>=5]['class']}))