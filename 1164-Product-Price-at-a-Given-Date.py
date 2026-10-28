import pandas as pd
import numpy as np

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products['change_date'] = pd.to_datetime(products['change_date'])
    p = products[products['change_date'] <= '2019-08-16']
    p = p.sort_values('change_date').drop_duplicates('product_id', keep='last')
    result = products[['product_id']].drop_duplicates().merge(
        p[['product_id', 'new_price']], on='product_id', how='left'
    )
    result['price'] = result['new_price'].fillna(10)
    return result[['product_id', 'price']]