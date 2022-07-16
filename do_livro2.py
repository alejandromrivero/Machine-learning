from collections import Counter
f=["alejandro","fabiana","alejandro", "fabiana alejandro",1,2,3,4,5,6,7,6,7,6,7,6,5,54,34,23,12]
c = Counter(f)
print(c)
print(c.most_common(5))
