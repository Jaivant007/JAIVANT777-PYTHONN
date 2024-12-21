import math
num = int(input("enter a number to check if it's a perfect square: "))
is_square = int(math.sqrt(num)) ** 2 == num
print(f"Is {num} a perfect square?", is_square)
