import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    s = sales.sort_values(by=['product_id', 'year']).reset_index(drop=True)
    r = s.groupby('product_id')['year'].transform('min')

    res = s[s['year'] == r]
    return res[['product_id', 'year', 'quantity', 'price']].rename(columns={'year':'first_year'})
    
