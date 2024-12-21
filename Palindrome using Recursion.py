def is_palindrome_rec(str_val):
    if len(str_val) <= 1:
        return True
    if str_val[0] != str_val[-1]:
        return False
    return is_palindrome_rec(str_val[1:-1])

str_val = input("enter a string to check if it's a palindrome: ")
print("Is the string a palindrome?", is_palindrome_rec(str_val))
