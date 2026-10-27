import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    m1=logs.merge(logs, left_on='id', right_on=logs["id"]-1, suffixes=('','_1'))
    m2=m1.merge(logs, left_on='id', right_on=logs["id"]-2, suffixes=('','_2'))

    n=m2[(m2['num']==m2['num_1']) & (m2['num']==m2['num_2'])]
    return n[['num']].drop_duplicates().rename(columns={'num':'ConsecutiveNums'})

