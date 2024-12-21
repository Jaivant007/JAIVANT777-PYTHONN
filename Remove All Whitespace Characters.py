def remove_whitespace(s):
    return "".join(s.split())

s = input("enter a string to remove all whitespace: ")
result = remove_whitespace(s)
print("String without Whitespace:", result)
