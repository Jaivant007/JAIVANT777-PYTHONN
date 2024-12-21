lst = list(map(int, input("enter elements of list separated by space: ").split()))
odd_sum = sum(x for x in lst if x % 2 != 0)
print("sum of odd numbers:", odd_sum)
