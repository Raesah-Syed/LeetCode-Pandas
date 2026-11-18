import pandas as pd

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    books=books[books['available_from']<'2019-05-23']
    orders=orders[orders['dispatch_date'].between('2018-06-23','2019-06-23')]
    m=orders.merge(books, on='book_id', how='right')
    e=m.groupby(['book_id','name'])['quantity'].sum().reset_index()
    e=e[e['quantity']<10]
    return (e[['book_id','name']])