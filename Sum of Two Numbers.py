def sum_recursive(a, b):
    if b == 0:
        return a
    return sum_recursive(a + 1, b - 1)

a, b = map(int, input("enter two numbers to sum (space-separated): ").split())
result = sum_recursive(a, b)
print("Sum:", result)
