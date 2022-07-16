import pandas as pd
import numpy as np
from Functions_Alejandro import contador_positivos, contador_positivosprinting, contador_negativos



a=pd.Series(np.random.randn(100))
print(a)
d=contador_negativos(a)
e=contador_positivos(a)

print('numeros negativos:',d,'\n','numeros positivos:',e)
if d>e:
    print('os numeros negativos sao mais do que os numeros positivos')
elif d<e:
    print('os numeros positivos sao mais do que os numeros negativos')
else:
    print('ha a mesma quantidade de numeros positivos e negativos')

