def common_characters(s1, s2):
    return set(s1) & set(s2)

s1 = input("enter the first string: ")
s2 = input("enter the second string: ")
result = common_characters(s1, s2)
print("common Characters:", result)
