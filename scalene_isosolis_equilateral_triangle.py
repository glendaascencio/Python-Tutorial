# Python-Tutorial
Tutorial for learning how to Program with python

''' We'll pront the user to enter the size of a triangle and
we'll determine if it is an scalene, isosolis, or equilateral triangle

* Scalene triangle= is when the sizes has different lenghts
* Isosceles triangle = has two equal lenghts
* Equilateral triangle = has three equal lengths
'''

a = int(raw_input("Enter the length of a = "))
b = int(raw_input("Enter the lenght of b = "))
c = int(raw_input("Enter the lenght of c = "))

if a != b and a != c and c != a:
    print("This is a scalene triangle")
elif a == b and b == c:
    print("This is a equilateral triangle")
else:
    print("This is an isosceles triangle")
