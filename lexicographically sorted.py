def is_lexicographically_sorted(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

print(is_lexicographically_sorted("abc"))
print(is_lexicographically_sorted("aab"))
print(is_lexicographically_sorted("zyx"))
print(is_lexicographically_sorted("apple"))
print(is_lexicographically_sorted("a"))
