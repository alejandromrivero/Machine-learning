import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(12).reshape(3,4), index=['Ohio','Colorado','New York'], columns=['one', 'two','three','four'])

print(data)
print('======================================================')
transform= lambda x: x[:4].upper()

data.index=data.index.map(transform)
print(data)

