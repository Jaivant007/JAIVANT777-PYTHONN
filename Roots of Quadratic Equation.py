import math
a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b: "))
c = float(input("enter coefficient c: "))
discriminant = b ** 2 - 4 * a * c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots of the quadratic equation: {root1}, {root2}")
else:
    print("No real roots")
