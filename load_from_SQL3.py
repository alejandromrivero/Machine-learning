import pymysql
import pandas as pd
import numpy as np

conn=pymysql.connect(host='localhost', port=3306,user='root', passwd='', db='teste')
cur=conn.cursor()
cur.execute("select * from countries WHERE country LIKE 'Cu%' AND addres_number<13500 ORDER BY entity_number")
'''for row in cur:
    print(row)
print('=================================================================================\n')
print('=================================================================================\n')
print('=================================================================================\n')'''
results=list(cur.fetchall())# esta parte es muy importante
#print(pd.DataFrame(results,index=np.arange(len(results)), columns=['entity_number','addres_number','addres1','addres2','country','remarks','reference']))
resultado=pd.DataFrame(results,index=np.arange(len(results)), columns=['entity_number','addres_number','addres1','addres2','country','remarks','reference'])
print(resultado)
resultado.to_csv('F:/dumps/salvando_desde_base_de_datos_MySQL.csv')
cur.close()
conn.close()