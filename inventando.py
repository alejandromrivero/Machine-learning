from matplotlib import pyplot as plt

import csv

a=[2,3,4,5,6,7,8,9,10]
b=[34,56, 78, 90, 43, 23, 123, 90, 34]

c=len(a)
zipped=dict(zip(a,b))
print(zipped)

plt.plot(a,b)
plt.show()


