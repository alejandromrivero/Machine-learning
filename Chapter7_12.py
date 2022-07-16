import pandas as pd
import numpy as np


df=pd.DataFrame(np.arange(200).reshape(50,4))
print(df)

sampler=np.random.permutation(50)
print(sampler)

print(df.take(sampler))
print(df.sample(n=5))


dff=pd.DataFrame({'key':['b','b','a','c','a','b'],'data':range(6)})
print(dff)
dummies=pd.get_dummies(dff['key'],prefix='key')
print(dummies)
'''dff_with_dummies=dff[['data1']].join(dummies)
print(dff_with_dummies)'''
