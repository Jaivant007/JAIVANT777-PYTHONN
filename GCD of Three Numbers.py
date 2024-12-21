import math
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
gcd = math.gcd(math.gcd(a, b), c)
print(f"GCD of {a}, {b}, and {c}: {gcd}")
