import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates()

    activities = activities.sort_values(by=['sell_date', 'product'])

    result = activities.groupby('sell_date').agg(
        num_sold=('product', 'count'),
        products=('product', lambda x: ','.join(x))
    ).reset_index()
    
    return result