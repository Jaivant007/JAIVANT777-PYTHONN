lst = list(map(int, input("enter elements of list separated by space: ").split()))
lst = list(set(lst))
lst.sort()
second_largest = lst[-2]
print("Second largest element is", second_largest)
