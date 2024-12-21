lst = list(map(int, input("enter elements of list separated by space: ").split()))
even_sum = sum(x for x in lst if x % 2 == 0)
print("sum of even numbers:", even_sum)
