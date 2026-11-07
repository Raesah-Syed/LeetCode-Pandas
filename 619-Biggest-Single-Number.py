import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my=my_numbers.value_counts().reset_index(name='c')
    my=my[my['c']==1]
    x = pd.DataFrame({'num': [my['num'].max()]})
    return(x)