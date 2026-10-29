import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer['visited_on'] = pd.to_datetime(customer['visited_on'])
    
    daily = customer.groupby('visited_on')['amount'].sum().reset_index()
    daily = daily.sort_values('visited_on')
    
    daily['amount'] = daily['amount'].rolling(window=7, min_periods=7).sum()
    daily['average_amount'] = (daily['amount'] / 7).round(2)
    
    result = daily.dropna().reset_index(drop=True)
    return result[['visited_on', 'amount', 'average_amount']]