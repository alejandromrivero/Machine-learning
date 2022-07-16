import pandas as pd
import numpy as np
#pd.options.display.max_rows = 100000
#pd.options.display.max_columns=10

with open('F:/dumps/4b676921-53e4-42a1-ae6e-210674ba0a4d_EULobbyingOrganizations.csv', 'rb') as entrada:
    ler = pd.read_csv(entrada, index_col='organization_name')
#print(ler)
df=pd.DataFrame(ler)
print(df.sort_values(by='country_head_office'))
print(df.loc['Armenian Women for Health and Healthy Environment'])
'''print(df['lobbyists_fte']>8)
print('asi son las cosas, marcador: -----------------------------------------------------------------------------\n',df.sort_index())
print(df.loc['South And East Consulting'])'''
print('las columnas de este son: \n',df.columns)
print('el indice de este es: \n', df.index)

f_out=df.sort_values(by='country_head_office')
#g_out=f_out['lobbyists_fte']
#print(g_out)
for row in f_out:#aqui estoy aislando una de las variables del documento.
    lobbyists_fte=f_out['lobbyists_fte']
    country=f_out['country_head_office']
print(len(lobbyists_fte),'registros \n', 'suma: \n',lobbyists_fte.sum(),'\n resumen estadistico: \n',lobbyists_fte.describe(),'\n','valores presentes vs frecuencias de aparicion: \n', lobbyists_fte.value_counts(),'\n','media:' ,lobbyists_fte.mean(),'\n',
      'minimo:',lobbyists_fte.min(),'\n','maximo:',lobbyists_fte.max())
IRQ= abs(lobbyists_fte.quantile(0.25)-lobbyists_fte.quantile(0.75))
print('iqr:',IRQ)
rango=lobbyists_fte.max()-lobbyists_fte.min()
kurtosis=lobbyists_fte.kurt()

print('rango:',rango)
print('kurtosis:',kurtosis)
print('cambio porcentual: \n',lobbyists_fte.pct_change())
#gf_out=
#print('la cantidad de indices con lobbyists_fte mayor que x es: \n',len(g_out))
#f_out.to_csv('F:/dumps/salvando_em_csv.csv', sep='|')
print('====================================================================================================================')
print(lobbyists_fte.sort_values())
print('====================================================================================================================')
print('AHORA TRABAJANDO CON LOS NOMBRES DE LOS PAISES DE ASIENTO DE ESTAS ORGANIZACIONES')

print(country.sort_values())
paises=country.value_counts()
print(paises)
pais=list(zip(paises,np.arange(len(paises))))
print('=================================PAIS PAIS PAIS======================================================================')
'''print(pais)
'''

plotando=pd.DataFrame(paises)
paises.to_csv('F:/dumps/plotando.csv')
print(plotando)


