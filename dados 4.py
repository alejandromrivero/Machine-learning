import csv

with open('F:\DATA SCIENCE BOOKS\code-python3 Data science from cratch\colon_delimited_stock_prices.txt','rb') as f:
    reader=csv.DictReader(f, delimiter='\t')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        print(date, symbol, closing_price)
