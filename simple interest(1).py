def calculate_simple_interest(principal, years, is_senior):
    if principal <= 0 or years <= 0:
        return 0
    rate = 0.12 if is_senior else 0.10
    interest = principal * years * rate
    return interest

principal = float(input("Enter the principal amount: "))
years = int(input("Enter the no of years: "))
is_senior_input = input("Is customer senior citizen (y/n): ").strip().lower()
is_senior = True if is_senior_input == 'y' else False

interest = calculate_simple_interest(principal, years, is_senior)
print(f"Interest: {interest}")

# Test Cases
print(calculate_simple_interest(2000, 0, False))  
print(calculate_simple_interest(20000, -2, False))  
print(calculate_simple_interest(-2000, 2, False))  
print(calculate_simple_interest(2, 2000, False))  
print(calculate_simple_interest(0, 5, False))  
