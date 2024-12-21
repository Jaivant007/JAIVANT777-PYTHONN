n = int(input("enter a number: "))
div_by_5 = [i for i in range(1, n + 1) if i % 5 == 0]
print(f"Numbers divisible by 5 in range 1 to {n}: {div_by_5}")
