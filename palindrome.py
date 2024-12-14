def is_palindrome(x):
    if isinstance(x, int):
        str_x = str(x)
        return str_x == str_x[::-1]
    else:
        return False

# Test cases
print(is_palindrome(121))  
print(is_palindrome(-121))  
print(is_palindrome(10))  
print(is_palindrome("abc"))  
print(is_palindrome(0))  
