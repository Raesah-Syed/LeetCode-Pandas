import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    max_id = customers['customer_id'].max()
    all_ids = pd.DataFrame({'ids': range(1, max_id + 1)})
    missing_ids = all_ids[~all_ids['ids'].isin(customers['customer_id'])]
    
    return missing_ids