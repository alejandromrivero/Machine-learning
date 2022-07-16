import re, csv
start_with_hash=0
with open('F:/dumps/Libro1.csv','rb') as f:
    for linha in f:
     if re.match("3", linha):
            start_with_hash+=1
    print(start_with_hash)
