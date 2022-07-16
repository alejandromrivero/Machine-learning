import csv
import pandas as pd
arquivo=pd.read_csv('F:\DATA SCIENCE BOOKS\code-python3 Data science from cratch\colon_delimited_stock_prices.txt')

#print(arquivo)
for row in arquivo :
    date = row["date"]
    symbol = row["symbol"]
    closing_price = float(row["closing_price"])
    print(date, symbol, closing_price)