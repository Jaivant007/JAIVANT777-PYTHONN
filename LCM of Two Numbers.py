import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = (a * b) // math.gcd(a, b)
print(f"LCM of {a} and {b} is {lcm}")
