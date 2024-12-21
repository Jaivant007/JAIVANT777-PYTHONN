def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

s = input("enter a string to get character frequencies: ")
result = char_frequency(s)
print("Character Frequencies:", result)
