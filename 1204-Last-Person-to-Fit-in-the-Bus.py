import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    sor=queue.sort_values(by='turn')
    sor['tot']=sor['weight'].cumsum()
    fit = sor[sor['tot'] <= 1000]
    return pd.DataFrame({'person_name': [fit.iloc[-1]['person_name']]})