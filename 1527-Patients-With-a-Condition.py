import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    c = patients['conditions']
    return patients[
        c.str.startswith('DIAB1') | 
        c.str.contains(' DIAB1', regex=False) | 
        c.str.contains('DIAB1 ', regex=False)
    ]