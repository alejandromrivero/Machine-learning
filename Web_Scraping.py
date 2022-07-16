import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

req=requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
if req.status_code==200:
    print('Respuesta bien sucedida')
    content=req.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all(name='table')
    table_str = str(table)
    df = pd.read_html(table_str)[0]
    df.to_csv('F:/DataFrame.csv')
leitura=pd.read_csv('F:/DataFrame.csv', sep=',', index_col=0)
lec=pd.DataFrame(leitura,index=np.arange(len(leitura)) ,columns=['Rk', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%',
       '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%',
       'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])
print(lec)
lec[lec['Rk']=='Rk']=np.nan
lec_u=lec.dropna()
print(lec_u)


    

