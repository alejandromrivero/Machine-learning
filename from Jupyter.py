import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.stats.tests.test_multi import NA
pd.options.display.max_rows=10000

entrada=pd.read_json('F:/dumps/SELECT____valor_bruto_ISS_valor_total_NF.json','rb')
dados=pd.DataFrame(entrada)
dados2=dados.set_index(['NFSe'])
#print(dados2.index)
#print(dados2.columns)
#print(dados2.sort_index())
#print(dados2.iloc[285])
ano_2017=dados2[dados2['emissao']<='2017-12-31']
ano_2018=dados2[dados2['emissao']>='2018-01-01']
print('2017 : \n',ano_2017['valor_nota'].sum())
print('2018 : \n',ano_2018['valor_nota'].sum())
print(ano_2017['valor_nota'].sum()+ano_2018['valor_nota'].sum())
print(ano_2017.sort_index())

data=pd.read_csv('F:\DATA SCIENCE BOOKS\pydata-book-2nd-edition\examples\macrodata.csv')
print(data.head())
