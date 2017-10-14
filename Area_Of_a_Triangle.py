# Writing a function that will return the area of a triangle = 1/2 * base * heigh
base = int(raw_input("Enter base a of triange: "))
height = int(raw_input("Enter heigh of triange: "))

def triangle_area(base, height):
    area = (1.0/2.0) * base * height
    print(area)
triangle_area(base, height)
