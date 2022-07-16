import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


leitura=pd.read_csv('F:/dumps/plotando.csv', names=['Pais','inst'])
#print(leitura)
print(leitura.sort_values(by='inst', ascending=False))


#xs=[i+0.1 for i, _ in enumerate(leitura['Pais']) ]
plt.bar(leitura['Pais'],leitura['inst'], color='orange')

plt.xticks([4 * i for i in range(len(leitura))], rotation=90, fontsize=5)
plt.grid(True,linestyle='dashed', color='grey', linewidth=0.4)
plt.axis([-5, 60, 0, 2200])
plt.show()

'''labels=leitura['Pais']
plt.pie(leitura['inst'], labels=labels )
plt.show()'''
