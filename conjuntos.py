from collections import Counter
s=set()#aqui el conjunto esta vacio.
s.add(1)
s.add(2)
s.add(3)
s.add(23)
x=len(s)
y= 2 in s
z=45 in s

print(s,[x],(y,z))
stopwords_list=["a","an","at"]+["yet", "you","if","the","the"]+["then"]
print(stopwords_list)
r1=Counter(stopwords_list)
r2="not" in stopwords_list
print(r1)
print(r2)
print(r1.most_common(3))
