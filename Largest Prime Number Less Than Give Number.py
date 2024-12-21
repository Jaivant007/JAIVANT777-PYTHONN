num = int(input("enter a number: "))
largest_prime = 0
for i in range(num - 1, 1, -1):
    if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
        largest_prime = i
        break
print(f"Largest prime number less than {num}: {largest_prime}")
