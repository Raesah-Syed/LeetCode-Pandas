import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    s=employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N < 1 or N > len(s):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    val = s.iloc[N - 1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [val]})
