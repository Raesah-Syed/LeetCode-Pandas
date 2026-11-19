import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    enrollments=enrollments.sort_values(by=['student_id','grade','course_id'], ascending=[True,False,True])
    enrollments['rank']=enrollments.groupby(['student_id'])['grade'].rank(method='first', ascending=False)
    return (enrollments[enrollments['rank']==1][['student_id','course_id','grade']])