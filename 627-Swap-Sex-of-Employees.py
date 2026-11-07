import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex']=numpy.where(salary['sex']=='m','f','m')
    return (salary)