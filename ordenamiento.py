from collections import Counter

x=[4,1,2,3,4,5,3,2,5,6,5,6,5,6,5,5,5,3]
y=x+[4,5,6]
ati={4,1,2,3,4,5,3,2,1,2,4,7,8,9,7,6,5,4,5,45,43,23,12,21,32,43,54,65,76,87,98,90}
print(len(y))
print(len(ati))
z=set(y)
d=Counter(y)

numbers_pairs=[y for y in range(6) if y%2==0]
squares=[y*y for y in numbers_pairs]

print(numbers_pairs)
print(squares)

g=len(ati)
print(sorted(ati))
square_dict=[at*at for at in ati]
print(sorted(square_dict))


