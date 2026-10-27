import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    r=person.merge(address, on="personId", how="left")
    return r[["firstName","lastName","city","state"]]