import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    even=employees[employees['employee_id']%2==0][['employee_id']]
    m=employees[employees['name'].str.startswith('M')][['employee_id']]
    overlapping_ids =  np.union1d(even['employee_id'], m['employee_id'])
    employees['bonus']=numpy.where(employees['employee_id'].isin(overlapping_ids),0,employees['salary'])
    return (employees[['employee_id','bonus']].sort_values(by='employee_id'))