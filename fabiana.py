import pymysql
import pandas as pd
import numpy as np
import datetime
from statsmodels.stats.tests.test_multi import NA
pd.options.display.max_rows=10000

'''data_1= input("entre uma data 1 no formato yyyy-mm-dd : ") #VER COMO HAGO ESTO
data_main1=datetime.strptime(data_1,"%Y/%m/%d")
data_2= input("entre uma data 2 no formato yyyy-mm-dd : ")
data_main2=datetime.strptime(data_2,"%Y/%m/%d")'''

conn=pymysql.connect(host='localhost', port=3306,user='root', passwd='', db='fabiana_empresa_tentativa')
cur=conn.cursor()
cur1=conn.cursor()
cur.execute("select * from razao")

results=list(cur.fetchall())# esta parte es muy importante
resultado=pd.DataFrame(results, index=np.arange(len(results)),
                       columns=['data','lote','lanc','historico','contrapartida','debito','credito','saldo','natureza'])


cur.close()
conn.close()
g=pd.DataFrame(resultado[resultado['debito']!=0])
print(g)

