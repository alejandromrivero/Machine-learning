import pandas as pd
import numpy as np

val='a,b,guido'

print(val)
print(val.split(','))

pieces=[x.strip() for x in val.split(',')]
print(pieces)
first,secong,third=pieces
print(first)
print(secong)
print(third)





