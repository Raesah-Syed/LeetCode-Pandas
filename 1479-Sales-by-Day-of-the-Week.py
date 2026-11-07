import pandas as pd

def sales_by_day(orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    orders['day'] = orders['order_date'].dt.day_name()

    g = orders.groupby(['item_id', 'day'])['quantity'].sum().reset_index()
    m = g.merge(items, on='item_id', how='right')

    p = m.pivot_table(
        index='item_category',
        columns='day',
        values='quantity',
        aggfunc='sum'
    ).fillna(0)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    p = p.reindex(
        index=items['item_category'].drop_duplicates().sort_values(),
        columns=days,
        fill_value=0
    )

    p.columns = p.columns.str.upper()

    return p.reset_index().rename(columns={'item_category': 'CATEGORY'})