def count_words(s):
    return len(s.split())

s = input("enter a string to count words: ")
result = count_words(s)
print("Number of Words:", result)
