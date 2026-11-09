import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    m=warehouse.merge(products, on ='product_id')
    m['volume']=m['Width']*m['Length']*m['Height']*m['units']
    r=m.groupby(['name'])['volume'].sum().reset_index()
    return r[['name','volume']].rename(columns={
        'name':'warehouse_name'
    })