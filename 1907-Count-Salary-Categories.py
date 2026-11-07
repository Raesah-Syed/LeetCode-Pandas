import pandas as pd
import numpy

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['sal']=numpy.where(accounts['income']<20000,'Low Salary','null')
    accounts['sal']=numpy.where(accounts['income'].between(20000,50000),'Average Salary',accounts['sal'])
    accounts['sal']=numpy.where(accounts['income']>50000,'High Salary',accounts['sal'])
    df=pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary']})
    res= df.merge(accounts, left_on='category', right_on='sal', how='left')
    return (res.groupby(['category'])['account_id'].nunique().reset_index().rename(columns={'account_id':'accounts_count'}))