import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    m1=school_a.merge(school_b, how='cross',suffixes=('a','b'))
    m2=m1.merge(school_c, how='cross')
    res=m2[(m2['student_ida']!=m2['student_idb']) & (m2['student_idb']!=m2['student_id']) & (m2['student_id']!=m2['student_ida']) & (m2['student_namea']!=m2['student_nameb']) & (m2['student_nameb']!=m2['student_name']) & (m2['student_name']!=m2['student_namea']) ]
    return (res[['student_namea','student_nameb','student_name']].rename(columns={
        'student_namea':'member_A',
        'student_nameb':'member_B',
        'student_name':'member_C',
    }))
  