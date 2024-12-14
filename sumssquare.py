def sumsquare(l):
    odd = sum(x**2 for x in l if x % 2 != 0)
    even = sum(x**2 for x in l if x % 2 == 0)
    return [odd, even]

l = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    element = int(input("Enter the element: "))
    l.append(element)

result = sumsquare(l)
print(result)
