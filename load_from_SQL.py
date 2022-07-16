import sqlite3
import pandas as pd
import numpy as np
import pyodbc


query=pyodbc.connect("DRIVER={pyodbc};server=localhost; database=parch & posey; uid=sa; pwd=sa")
cur=query.cursor()
cur.execute("select website from accounts")
for row in cur:
    print (row.website,',',row.name)
cur.close()
query.close()
