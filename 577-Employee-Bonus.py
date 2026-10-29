import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    m=employee.merge(bonus, on='empId', how='left', suffixes=('','_y'))
    m['bonus']=m['bonus']
    return (m[(m['bonus'].isna()) | (m['bonus']<1000)][['name','bonus']])