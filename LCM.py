import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a, b = map(int, input("enter two numbers for LCM (space-separated): ").split())
result = lcm(a, b)
print("LCM:", result)
