def sort_names(names, order):
    if order.upper() == 'A':
        return sorted(names)
    elif order.upper() == 'D':
        return sorted(names, reverse=True)
    else:
        return names

names = []
n = int(input("Enter the number of names: "))
for _ in range(n):
    name = input("Enter the name: ")
    names.append(name)

order = input("Order (A/D): ")

sorted_names = sort_names(names, order)
for name in sorted_names:
    print(name)
