# importing pandas

import pandas as pd

# Creating Dictionary
a = {'id': [1, 2, 10, 12], 
	'val1': ['a', 'b', 'c', 'd']}

b = {'id': [1, 2, 9, 8],
	'val1': ['p', 'q', 'r', 's']}

d1 = pd.DataFrame(a)

d2 = pd.DataFrame(b)

pd.merge(d1,d2,on='id',how='inner')

d1.merge(d2,on='id', how='inner')

d1.merge(d2,on='id', how='left')