import pymysql
import pandas as pd

conn=pymysql.connect(host='localhost', port=3306,user='root', passwd='', db='teste')
cur=conn.cursor()
cur.execute("select * from countries")
#print('descripcion de cur: \n',cur.description)
for row in cur:
    print(row)
print('=================================================================================\n')
print('=================================================================================\n')
print('=================================================================================\n')
results=cur.fetchall()
print(results)
cur.close()
conn.close()

