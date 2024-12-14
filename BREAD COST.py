def calculate_bread_cost(fresh_loaves, day_old_loaves):
    regular_price = 185.00
    discount = 0.60
    fresh_cost = fresh_loaves * regular_price
    day_old_cost = day_old_loaves * regular_price * (1 - discount)
    total_cost = fresh_cost + day_old_cost
    return regular_price, fresh_cost, day_old_cost, total_cost

fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day old loaves purchased: "))

regular_price, fresh_cost, day_old_cost, total_cost = calculate_bread_cost(fresh_loaves, day_old_loaves)

print(f"Regular price: Rs.{regular_price:.2f}")
print(f"Amount of new loaves: Rs.{fresh_cost:.2f}")
print(f"Amount of day old loaves: Rs.{day_old_cost:.2f}")
print(f"Total amount: Rs.{total_cost:.2f}")
