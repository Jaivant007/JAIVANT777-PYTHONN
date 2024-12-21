import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = float(input("enter the radius of the circle: "))
result = area_of_circle(radius)
print("Area of the Circle:", result)
