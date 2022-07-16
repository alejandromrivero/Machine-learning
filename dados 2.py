import csv
with open('F:/DATA SCIENCE BOOKS/code-python3/tab_delimited_stock_prices.txt','rb') as f:
    reader=csv.reader(f,delimiter='\t')
    for row in reader:
        date=row[0]
        symbol=row[1]
        closing_price=float(row[2])
        print (date,symbol,closing_price)