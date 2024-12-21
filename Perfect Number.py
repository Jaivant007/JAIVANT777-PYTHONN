def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

n = int(input("enter a number to check if it's perfect: "))
result = is_perfect_number(n)
print("Perfect Number:", result)
