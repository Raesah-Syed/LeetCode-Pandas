import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    x=person[person.duplicated(subset=['email'])]
    return x[['email']].drop_duplicates().rename(columns={'email':'Email'})