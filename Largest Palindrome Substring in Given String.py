def longest_palindrome(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    max_palindrome = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(max_palindrome):
                max_palindrome = substring
    return max_palindrome

s = input("enter a string to find the longest palindrome substring: ")
result = longest_palindrome(s)
print("longest palindrome substring:", result)
