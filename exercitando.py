from functools import partial

from dill.tests.test_mixins import doubler

from herr_funcionales import exp

'''power=float(input("entre un numero para asumir la variable power: "))
two_to_the=partial(exp,2)
print(two_to_the(power))
from dill.tests.test_mixins import doubler'''

from herr_funcionales import double

numero=input("entre un numero para hacer una lista: ")
s=int(numero)
print(s)
xs=list(range(s))
print("xs= ",xs)

twice_xs=[double(x) for x in xs]
#twice_xs=map(double,xs)
twice_xs1=double(xs)
print("double de xs= ", twice_xs)
print("double de xs= ", twice_xs1)


