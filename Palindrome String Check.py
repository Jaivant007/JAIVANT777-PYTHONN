str_val = input("enter a string to check if it's a palindrome: ")
is_palindrome = str_val == str_val[::-1]
print("Is the string a palindrome?", is_palindrome)
