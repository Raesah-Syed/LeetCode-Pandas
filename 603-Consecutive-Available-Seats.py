import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema['g']=cinema.groupby(['free']).rank(method='first')
    cinema=cinema[cinema['free']==1]
    cinema['group']=cinema['seat_id']-cinema['g']
    cinema['c']=cinema.groupby(['group'])['seat_id'].transform('count')
    return pd.DataFrame(cinema[cinema['c']>=2]['seat_id']).sort_values(by=['seat_id'])