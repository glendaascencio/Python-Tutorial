# Python-Tutorial
Tutorials for Learning how to Program with python

# Printing the size of a list and a tuple
import sys
list_ex = [1, 2, 3, 4]
tuple_ex = (1, 2, 3, 4)

print("List size = ", sys.getsizeof(list_ex))
print("tuple size = ", sys.getsizeof(tuple_ex))

# Working with timeit
import timeit
list_test = timeit.timeit(stmt="[1, 2, 3]", number = 1000000)
tupes_test = timeit.timeit(stmt="(1, 2, 3)", number = 1000000)

print("List test time", list_test)
print("Tupes test time", tupes_test)


# Analyzing surveys with tuples
survey = (24, "Honduras", True)
age = survey[0]
place = survey[1]
knows = survey[2]
print("Age = ", age, "Place = ", place, "Knows Python = ", knows)

# Analyzing survey in a faster way
survey2 = (23, "Mexico", False)
age, place, knows_python = survey2
print("Age = ", age)
print("Place = ", place)
print("Knows Python = ", knows_python)

# Printing the variable table in Python
a = "glenda"
print(type(a))

''' ####       Boolean conversions ####
triveal are concerted to False
while non-triveal are converted to True
'''

# Allowing people enter an input 
name = raw_input("Please enter your name: ")
last_name = raw_input("Please enter your last name: ")
print ("Your first name is: " + name + " and your last name is: " + last_name)
