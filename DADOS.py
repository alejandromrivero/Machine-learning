import pandas as pd

#entrada_dados=open('F:/dumps/argumentos1.txt')
with open('F:/dumps/argumentos1.txt', 'r') as entrada:
    ler = pd.read_table(entrada)
    print (ler)