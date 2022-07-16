import csv


with open('F:/dumps/FDA.csv', 'r') as entrada:
    ler = csv.reader(entrada)
    for linha in ler:
        print (linha)
