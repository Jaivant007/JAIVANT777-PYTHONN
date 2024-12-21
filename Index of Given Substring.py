def find_substring_index(s, substring):
    return s.find(substring)

s = input("enter a string: ")
substring = input("enter the substring to find: ")
result = find_substring_index(s, substring)
print("Index of Substring:", result)
