import random
from matplotlib import pyplot as pl
x=int(input("entre un numero para conformar as listas:   "))
element1=list(range(x))
element2=list([random.random() for _ in range(x)])
a=list(zip(element1,element2))

print("element1= ",element1)
print("element2= ",element2)
print("a= ",a)
pl.plot(element1,element2)
pl.show()



