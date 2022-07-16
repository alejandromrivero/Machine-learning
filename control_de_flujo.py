from random import randint
import numpy as np

c=float(input("entre un numero: "))
d=float(input("entre el segundo numero: "))
if c>d:
    print(c, "es mayor que ",d)
    while c>d:
        d+=0.0000012*randint(5,9)
        c-=0.0000034*randint(-9,9)
        g=[d,c]
        print(g,c-d,"->")
        if d-c>2:
            continue
        if d-c<0.01:
            break
else:
    print(d, " es mayor que ",c)
    while d>c:
        c +=0.00055*randint(5,9)
        d-=0.000345*randint(-9,9)
        g=[c,d]
        print(g,d-c)
        if d-c>2:
            continue
        if d-c<0.01:
            break
