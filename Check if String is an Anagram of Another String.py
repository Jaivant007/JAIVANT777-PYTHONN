def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input("enter the first string: ")
s2 = input("enter the second string: ")
result = is_anagram(s1, s2)
print("Is anagram it?", result)
