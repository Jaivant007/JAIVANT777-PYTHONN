email = input("enter an email address: ")
is_valid_email = "@" in email and "." in email.split("@")[1]
print(f"Is the email valid? {is_valid_email}")
