import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



#entrada=open('F:/dumps/select___from_accounts.csv')
with open('F:/dumps/select___from_accounts.csv','rb') as entrada:
    ler = pd.read_csv(entrada)
    for row in ler:
        ident=ler['id']
        nome=ler['name']
        site=ler['website']
        latitude=ler['latit']
        longitude = ler['longit']
        contato_inicial=ler['primary_poc']
        posicion = list(zip(latitude, longitude))
        nova_linha=[ident, nome, posicion, site]
    #print(nova_linha)
    print(len(posicion), 'registros')
    print(posicion)
plt.scatter(latitude,longitude, marker='.', color='black')
plt.title('Scatter plot of position', fontsize=14, color='brown')
plt.xlabel('Latitude', color='black', fontstyle='italic', fontsize=14)
plt.ylabel('Longitude', color='grey', fontstyle='italic', fontsize=14)
plt.grid(True, linewidth=0.1, linestyle='--', color='grey')
plt.savefig('F:/dumps/cosa1.png', format='png')
plt.show()











