import pandas as pd
import numpy as np

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    s = np.where(
        seat['id'] % 2 != 0,
        seat['student'].shift(-1),
        seat['student'].shift(1)
    )
    seat['student'] = pd.Series(s).fillna(seat['student'])
    return seat[['id', 'student']]