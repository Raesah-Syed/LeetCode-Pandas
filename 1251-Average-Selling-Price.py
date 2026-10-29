import pandas as pd
import numpy as np

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on='product_id', how='left')

    valid = (df.purchase_date >= df.start_date) & (df.purchase_date <= df.end_date)
    df['units'] = df['units'].where(valid, 0).astype(float)   # force numeric
    df['revenue'] = df['units'] * df['price'].astype(float)

    g = df.groupby('product_id')[['revenue', 'units']].sum()

    # replace 0 units with NaN BEFORE dividing, then fill the result with 0
    g['average_price'] = (g['revenue'] / g['units'].replace(0, np.nan)).fillna(0).round(2)

    return g.reset_index()[['product_id', 'average_price']]