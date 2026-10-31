import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    t=teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    return (t.rename(columns={'subject_id':'cnt'}))