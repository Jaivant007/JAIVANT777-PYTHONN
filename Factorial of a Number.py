num = int(input("enter a number to calculate its factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num}: {fact}")
