import pandas as pd
import numpy as np
from statsmodels.stats.tests.test_multi import NA

df=pd.DataFrame(np.random.rand(7,7), index=np.arange(7))
df.iloc[0:4,1:5]=NA
df.iloc[5:,5:7]=NA
print(df)
print('indice completo: \n',df.dropna())

'''de=df.iloc[4]
print('de: \n',de)
print('=================================================================================')
dg=df[3]
print('df: \n',dg)'''
print('=================================================================================')
dh=df.fillna({1:df[1].median(),2: df[2].mean(),3:df[3].mean(), 4:df[4].median(),5:df[5].mean(),6:df[6].median()})
print('dh: \n',dh)