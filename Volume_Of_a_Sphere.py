# Writing a function that will return the volumen of the sphere when given the radies
import math
radies = int(raw_input("Enter the radies of the sphere: "))
def sphere_volumen(radies):
    volumen = (4.0/3.0) * math.pi * radies**3
    print(volumen)

sphere_volumen(radies)
