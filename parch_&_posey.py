import csv
import pandas as pd
import numpy as np
pd.options.display.max_rows = 100000

dado=pd.read_csv('C:/wamp64/tmp/salvando_query_parch_&_posey.csv', names=['empresa','data', 'quantidade','qty_postada','vendas'], sep='\t', index_col=['empresa','data'], header=None)
base=pd.DataFrame(dado)
print(base.sort_values(by=['empresa','data']))
#print(base.sort_values('empresa'))
#print(base.sort_values(by='qty_postada'))
#print(base.sort_values(by=['data','empresa']))
#print(base.count())

