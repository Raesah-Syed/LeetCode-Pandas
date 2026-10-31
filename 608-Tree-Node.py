import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    m = tree.merge(tree, left_on='p_id', right_on='id', how='left', suffixes=('', '_p'))
    x = m['p_id'].drop_duplicates()
    m['type'] = np.where(m['id'].isin(x), 'Inner', 'Leaf')
    m['type'] = np.where(m['p_id'].isna(), 'Root', m['type'])
    return m[['id', 'type']]