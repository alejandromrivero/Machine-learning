
"""print("hello \nmundo")"""
from datetime import date

n=float(input("escreva a sua idade:  "))
m=int(input("digite a idade de sua namorada "))
hj = date.today()
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
print("hello mundo")

print("hello mundo, meu nome e Alejandro e tenho ",n," anos e esou escrvendo  hoje",dias[hj.weekday()]," ",hj)
print(int(n+m), "anos")
