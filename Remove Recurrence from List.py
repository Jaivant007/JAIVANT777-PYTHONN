lst = list(map(int, input("enter elements of list separated by space: ").split()))
lst = list(set(lst))
print("list after removing duplicates:", lst)
