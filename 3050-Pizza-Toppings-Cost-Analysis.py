import pandas as pd

def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:
    toppings.sort_values(by='topping_name')
    top1=toppings.merge(toppings, how='cross', suffixes=('1','2'))
    top1=top1[top1['topping_name1']<top1['topping_name2']]
    top2=top1.merge(toppings, how='cross', suffixes=('','3'))
    top2=top2[top2['topping_name2']<top2['topping_name']]
    top2['pizza']=top2['topping_name1']+','+top2['topping_name2']+','+top2['topping_name']
    top2['total_cost']=(top2['cost1']+top2['cost2']+top2['cost']).round(2)
    return (top2.sort_values(by=['total_cost','pizza'], ascending=[False,True])[['pizza','total_cost']])
    
    