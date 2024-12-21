from functools import reduce

def longest_word(words):
    return reduce(lambda x, y: x if len(x) > len(y) else y, words)

words = input("enter words (space-separated): ").split()
result = longest_word(words)
print("Longest Word:", result)
