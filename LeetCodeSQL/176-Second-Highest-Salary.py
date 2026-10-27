import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    uni=employee["salary"].drop_duplicates()

    if len(uni)<2:
        return pd.DataFrame({"SecondHighestSalary":[None]})
    
    sec=uni.nlargest(2).iloc[-1]
    return pd.DataFrame({"SecondHighestSalary":[sec]})