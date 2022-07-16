import pymysql
import pandas as pd
import numpy as np
from statsmodels.stats.tests.test_multi import NA
pd.options.display.max_rows=10000


conn=pymysql.connect(host='localhost', port=3306,user='root', passwd='', db='socios_eletronica')
cur=conn.cursor()
cur1=conn.cursor()
cur.execute("select * from estoque_rafael")
cur1.execute("SELECT DISTINCT Mercadoria ,sum(Quant) from estoque_rafael GROUP BY Mercadoria ORDER BY Mercadoria")

results=list(cur.fetchall())# esta parte es muy importante
results1=list(cur1.fetchall())
resultado=pd.DataFrame(results,index=np.arange(len(results)),columns=['Doc_de','ordem','Fornecedor','Cod_Forn','NF','Data','Cod_Prod','Cod_Fabric','Mercadoria','Quant','Preco_Unit','Total','Desconto','custo_total','Valor_em_NF','Forma_de_pagamento','1_Vencimento','Valor_1ro_Venc','2_Vencimento','Valor_2_Venc','3_Vencimento','Valor_3_Venc','Valor_ICM','Valor_IPI','Total_consumido','Em_estoque_ainda','Valor_em_estoque','Baixa_1','Orc_1','Baixa_2','Orc_2','Baixa_3','Orc_3','Baixa_4','Orc_4','Baixa_5','Orc_5','Baixa_6','Orc_6','Baixa_7','Orc_7','Baixa_8','Orc_8','Baixa_9','Orc_9','Baixa_10','Orc_10','Baixa_11','Orc_11','Baixa_12','Orc_12'])
resultado1=pd.DataFrame(results1, index=np.arange(len(results1)),columns=['Mercadoria', 'Quantidade'])
#print(resultado)
#resultado.to_csv('F:/dumps/salvando_desde_base_de_datos_MySQL.csv')
cur.close()
conn.close()
#print(resultado[resultado['Mercadoria']=='CABO DE REDE LAN UTP DE REDE CAT 5'])
p=resultado1.sample(frac=0.15)
g=pd.DataFrame(p)
print(g[['Quantidade','Mercadoria']].sort_index())
#print(g.index)
k=g[g['Quantidade']>=50]
print(k)
