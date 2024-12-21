def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

s = input("enter a string to find the first non-repeating character: ")
result = first_non_repeating_char(s)
print("first non-repeating character:", result)
