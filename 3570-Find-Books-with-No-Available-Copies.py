import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    borrowing_records['return_date']=pd.to_datetime(borrowing_records['return_date'])
    br=borrowing_records[borrowing_records['return_date'].isna()]
    brg=br['book_id'].value_counts().reset_index()
    
    m=library_books.merge(brg, on='book_id')
    res=m[m['count']==m['total_copies']]

    return (res[['book_id','title','author','genre','publication_year','count']].sort_values(by=['count','title'], ascending=(False,True)).rename(columns={
        'count':'current_borrowers'
    }))