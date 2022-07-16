import random
from collections import Counter

from numpy.core.defchararray import upper

f=int(input("entre un numero de elementos: "))

def mi_funcion(f):
    if f>50:
        a=range(f)
        b=[random.random() for _ in range(len(a))]
        print(a)
        print(b)
        c=list(zip(a,b))
        print("c= ",c)
        print("el numero de elementos de c es: ",len(c))
    else:
        a=(range(f))
        b=[random.random() for _ in range(len(a))]
        print(a)
        print(b)
        c=list(zip(b,a))
        print("c= ",c)
    print(upper("a partir de ahora se veran los tres elementos: a,b y c: "))
    print(a)
    print(b)
    print(c)

mi_funcion(f)

