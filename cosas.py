import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import seaborn as sb

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

with open('F:/dumps/4b676921-53e4-42a1-ae6e-210674ba0a4d_EULobbyingOrganizations.csv', 'rb') as entrada:
    ler = pd.read_csv(entrada)

#indice=ler['organization_name']
#df=pd.DataFrame(ler,index=indice, columns=['country_head_office','lobbying_costs','ep_passes','lobbyists_fte','number_of_meetings','registered_date','registered_date_unparsed'])
dg=pd.DataFrame(ler, columns=['organization_name','country_head_office','lobbying_costs','ep_passes','lobbyists_fte','number_of_meetings','registered_date','registered_date_unparsed'])
#print(df)
print(ler)
print('dg= \n', dg)
print(dg.sort_values(by='organization_name'))
#print('los indices de df son: \n', df.index)
#print('las columnas de df son: \n', df.columns)
#print(df.loc['European Committee for Homeopathy'])


