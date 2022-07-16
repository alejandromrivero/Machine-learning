import pandas as pd
import numpy as np
#pd.options.display.max_rows = 100000

columnas=['prim','seg','terc','qua']

indice=['havana', 'santiago','matanzas']
frame=pd.DataFrame(np.arange(12).reshape(3,4), index=indice, columns=columnas)
print(frame)
print(frame.rename(index=str.title,columns=str.upper))

fr=pd.Series(['a','d','d','f','t','a'])
frozen=pd.DataFrame(fr, index=np.arange(len(fr)),columns=['letra'])
print(fr.value_counts(sort=True))

hf=np.random.random_integers(2,90,1000)
hfg=pd.DataFrame(hf.reshape(500,2), index=np.arange(500), columns=['primeira','segunda'])
print(hfg)
print(hfg['segunda'].value_counts())

print(hfg.rename(columns=str.upper))



