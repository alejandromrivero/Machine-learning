import pandas as pd
import numpy as np

'''data=pd.DataFrame(np.arange(20).reshape(4,5), index=['a','b','c','d'], columns=['1','2','3','4','5'])
print(data)
data['5']='-'
print(data)
print(data.dropna(how='all'))
print(data.describe())'''

data=pd.DataFrame([[1,6.5,3],[1,None,None],[None,None,None],[None,6.5,3]])
print(data)
print(data.dropna(how='all', axis=1))
data[4]=None
print(data)
b=data.dropna(axis=1,how='all')
print(b)


