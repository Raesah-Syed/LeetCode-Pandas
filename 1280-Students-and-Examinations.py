import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # 1. Every student x every subject
    df = students.merge(subjects, how='cross')

    # 2. Count exams per (student, subject)
    counts = (examinations
              .groupby(['student_id', 'subject_name'])
              .size()
              .reset_index(name='attended_exams'))

    # 3. Attach counts; combos with no exams become NaN, so fill with 0
    df = df.merge(counts, on=['student_id', 'subject_name'], how='left')
    df['attended_exams'] = df['attended_exams'].fillna(0).astype(int)

    # 4. Order as required
    return df.sort_values(['student_id', 'subject_name'])[
        ['student_id', 'student_name', 'subject_name', 'attended_exams']
    ]