validate_password = lambda pwd: len(pwd) >= 8 and any(c.isdigit() for c in pwd) and any(c.islower() for c in pwd) and any(c.isupper() for c in pwd)

pwd = input("enter a password to validate: ")
result = validate_password(pwd)
print("Valid Password:", result)
