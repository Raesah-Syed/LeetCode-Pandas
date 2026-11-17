import pandas as pd

def geography_report(student: pd.DataFrame) -> pd.DataFrame:
    student=student.sort_values(by='name')
    student['row_num']=student.groupby('continent').cumcount()
    m=student.pivot(
        index='row_num',
        columns='continent',
        values='name'
    ).reset_index()
    return (m.reindex(columns=['America','Asia','Europe']))