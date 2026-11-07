import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    p = products[products['description'].str.contains(r'\bSN\d{4}\-\d{4}\b', na=False)]
    return p.sort_values(by='product_id')
