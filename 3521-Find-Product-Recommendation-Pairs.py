import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    mp=product_purchases.merge(product_purchases, on='user_id', suffixes=('1','2'))
    fp=mp[mp['product_id1']<mp['product_id2']]
    g=fp.groupby(['product_id1','product_id2'])['user_id'].nunique().reset_index()
    fg=g[g['user_id']>=3]
    h = product_info.merge(fg,left_on=['product_id'], right_on=['product_id1'])
    r = product_info.merge(h,left_on=['product_id'], right_on=['product_id2'], suffixes=('_1',''))
    #print(r)
    res=r[['product_id1','product_id2','category','category_1','user_id']].rename(columns=({'product_id1':'product1_id', 'product_id2':'product2_id','category':'product1_category','category_1':'product2_category','user_id':'customer_count'}))
    return res.sort_values(by=['customer_count','product1_id','product2_id'], ascending=[False,True,True])