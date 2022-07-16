import csv


today_prices={'AAPL': 90.91,'MSFT': 41.68,'FB':64.5}
with open("F:/DATA SCIENCE BOOKS/code-python3 Data science from cratch/comma_delimited_stock_prices.txt", 'wb') as f:
    writer=csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow(stock, price)
        print (stock,price)


#print (f)
