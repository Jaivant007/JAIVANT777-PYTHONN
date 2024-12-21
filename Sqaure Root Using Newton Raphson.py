import math
x = float(input("enter a number to find its square root: "))
guess = x / 2
epsilon = 0.01
while abs(guess * guess - x) > epsilon:
    guess = (guess + x / guess) / 2
print(f"Square root of {x} is", guess)
