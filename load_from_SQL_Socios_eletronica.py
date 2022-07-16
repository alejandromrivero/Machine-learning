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

conn=pymysql.connect(host='localhost', port=3306,user='root', passwd='', db='socios_eletronica')
cur=conn.cursor()
cur1=conn.cursor()
cur.execute("select * from estoque_rafael")
cur1.execute(" SELECT sum(despesa_por_NF) FROM"
                 "(SELECT NF,Data, round(sum(Total),2) despesa_por_NF FROM  "
                    "(SELECT NF,Data, Total FROM produtos_por_NF WHERE NF!='S/N' AND (Data BETWEEN '2017-12-01' AND '2018-04-01') AND Cod_Fabric LIKE '1%' "
                    "ORDER BY NF,Data) sub "
                  "GROUP BY NF,Data ORDER by Data)sub "
             "")

results=list(cur.fetchall())# esta parte es muy importante
results1=list(cur1.fetchall())
resultado=pd.DataFrame(results,index=np.arange(len(results)),columns=['Doc_de','ordem','Fornecedor','Cod_Forn','NF','Data','Cod_Prod','Cod_Fabric','Mercadoria','Quant','Preco_Unit','Total','Desconto','custo_total','Valor_em_NF','Forma_de_pagamento','1_Vencimento','Valor_1ro_Venc','2_Vencimento','Valor_2_Venc','3_Vencimento','Valor_3_Venc','Valor_ICM','Valor_IPI','Total_consumido','Em_estoque_ainda','Valor_em_estoque','Baixa_1','Orc_1','Baixa_2','Orc_2','Baixa_3','Orc_3','Baixa_4','Orc_4','Baixa_5','Orc_5','Baixa_6','Orc_6','Baixa_7','Orc_7','Baixa_8','Orc_8','Baixa_9','Orc_9','Baixa_10','Orc_10','Baixa_11','Orc_11','Baixa_12','Orc_12'])
resultado1=pd.DataFrame(results1, index=np.arange(len(results1)), columns=['despesa_total'])

cur.close()
conn.close()
print(resultado1)
print('suma total de las notas fiscales es de: R$',resultado[resultado['Orc_4']!='']['Total'].sum())