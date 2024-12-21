from collections import Counter

def second_most_frequent(s):
    count = Counter(s)
    most_common = count.most_common()
    return most_common[1][0] if len(most_common) > 1 else None

s = input("enter a string to find the second most frequent character: ")
result = second_most_frequent(s)
print("second most frequent character:", result)
