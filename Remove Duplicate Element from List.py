lst = list(map(int, input("enter elements of list separated by space: ").split()))
lst = list(dict.fromkeys(lst))
print("list after removing duplicates:", lst)
