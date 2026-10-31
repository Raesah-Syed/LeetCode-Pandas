import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    x=company[company['name']=='RED'][['com_id']]
    y=orders[orders['com_id'].isin(x['com_id'])]
    return (sales_person[~
        sales_person['sales_id'].isin(y['sales_id'])
        ][['name']])