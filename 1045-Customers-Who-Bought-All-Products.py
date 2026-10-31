import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer['c'] = customer.groupby('customer_id')['product_key'].transform('nunique')
    y=product['product_key'].nunique()
    return (customer[customer['c']==y][['customer_id']].drop_duplicates())