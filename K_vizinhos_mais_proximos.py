import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier

datos=pd.read_csv('F:/dumps/KNN/dados transporte empleados.csv',sep=';',
                  index_col='Employee ID')
data=pd.DataFrame(datos)
df=data.drop_duplicates()
df2=df.replace({'GENDER':{'F':1,'M':2,'U':1},'MARITAL STATUS':{'S':1,'M':2},
                'Mode':{'Car':1,'Public Transportation':2,'Bike':3}})
df2.to_csv('F:dumps/for_knn.csv')
dat=pd.read_csv('F:/dumps/for_knn.csv',sep=',', index_col='Employee ID')
datos_entrada=df2[['GENDER','Age','MARITAL STATUS','DriveDistanceMiles']]
datos_target=df2['Mode']
X_train,X_test,y_train,y_test=train_test_split(datos_entrada,datos_target)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))
dat_pred=pd.read_csv('F:/dumps/KNN/missingemployees.csv',sep=',',
                  index_col='Employee ID')
dat_pred2=dat_pred.replace({'GENDER':{'F':1,'M':2,'U':1},
                            'MARITAL STATUS':{'S':1,'M':2}})
print(dat_pred2['MARITAL STATUS'].unique())
dat_pred2['Mode']=knn.predict(dat_pred2)
#print(dat_pred2.drop_duplicates().sort_index())
print(dat_pred2.drop_duplicates().sort_index().replace({'GENDER':{1:'Female',2:'Male'},
                                                        'MARITAL STATUS':{1:'Single',2:'Married'},
                                                        'Mode':{1:'Car',2:'Public Transportation',3:'Bike'}}))



