set1 = set(map(int, input("enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("enter elements of second set separated by space: ").split()))
intersection_set = set1 & set2
print("intersection of sets:", intersection_set)
