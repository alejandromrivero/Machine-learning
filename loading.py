import pandas as pd

read=pd.read_csv('F:/dumps/salvando_desde_base_de_datos_MySQL.csv')
#print(read)
print(read.sort_values(by='addres_number'))
print('=====================================================================')
print(read[read['addres_number']>3000])
print('=====================================================================')
print(read.dropna(how='all'))
print(read['remarks'].isnull)