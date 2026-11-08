import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    nad=students.merge(departments, left_on='department_id', right_on='id', how='left',suffixes=('','_y'))
    nad=nad[nad['id_y'].isna()]
    return (nad[['id','name']])
