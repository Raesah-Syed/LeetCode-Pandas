import pandas as pd

def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:
    s=employee.sort_values(by=['company','salary'])
    s['rank']=s.groupby(['company'])['salary'].rank(method='first')
    s['c']=s.groupby(['company'])['id'].transform('nunique')
    s['m1']=(s['c']//2)+1
    s['m2']=(s['c']+1)//2
    s = s[(s['rank'] == s['m1']) | (s['rank'] == s['m2'])]
    return (s[['id','company','salary']].drop_duplicates(['company','salary']))
