integer_list = [1, 2, 3]
heterogeneus_list = ["string", 0.1, True]
list_fo_list = [integer_list, heterogeneus_list, []]

print(len(integer_list))
print(sum(integer_list))
x = (range(10))
print(x)
zero = x[0]
print(zero)
one = x[1]
print(one)

nine = x[-1]
print(nine)

eight = x[-2]
print(eight)
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(y), '+', len(x), '=', len(x) + len(y))

first_three = y[:3]
print(first_three)
three_to_end = y[3:]
print(three_to_end)
one_to_four = y[1:5]
print(one_to_four)

last_three = y[-3:]
print(last_three)
without_first_and_last = y[1:-1]

print(without_first_and_last)
copy_of_y = y[:]
print(copy_of_y)

message = 1 in copy_of_y
print(message)

print("concatenando listas de diversas formas")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)
print(x + [4, 5, 6])

print("y=", x.append(4))
a, b = [1, 2]
print(a)
print(b + a - a - a)
d = _, b = 1, 2
print(_, b)
print("tuplas")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuplas#
print("lista es ", my_list)
print("tupla es ", my_tuple)
my_list[1] = 78
print(my_list)


def sum_and_product (x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)
print("sp=", sp)
print("s= ", s, "p= ", p)

print("Diccionarios")
empty_dict = {}
print(empty_dict)
empty_dict2 = dict()
print(empty_dict2)
grades = {"Alejandro": 37, "Fabiana": 40, "marlene": 70}
print(grades)
marlene_grades = grades["marlene"]
print(marlene_grades)
fabiana_has_grade = "Fabiana" in grades
print(fabiana_has_grade)

fabiana_grade = grades.get("Fabia", 0)
print(fabiana_grade)
grades["Tim"] = 99
grades["Kate"] = 45
grades["Andres"] = 78
andres_grades = grades["Andres"]
print("andres_grades es ", andres_grades)
print(grades)
print(len(grades) + 6 - grades["Alejandro"])

grades_llaves = grades.keys()
grades_valores = grades.values()
grades_items = grades.items()
print(grades_llaves)
print(grades_valores)
print(grades_items)
"Alejandro" in grades_llaves
print("Alejandro" in grades_llaves)
print("Defaultdict")
document = ["A continuación, se creará un par de variables a modo de ejemplo. "]

from collections import Counter
c = Counter([document])
print(c)
