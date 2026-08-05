# Python Day 4: Operators
# Date: 03 Aug 2026

# Exercise 1: Predict Output
# 1. print(10 + 5) → 15
# 2. print(10 - 5) → 5
# 3. print(10*5) → 50
# 4. print(10/3) → 3.3333333333333335
# 5. print(10//3) → 3
# 6. print(10%3) → 1
# 7. print(2**3) → 8
# 8. print(10 > 5) → True
# 9. print(10 < 5) → False
# 10. print(10 == 10) → True
# 11. print(10 != 5) → True
# 12. print(10 >= 5) → True
# 13. print(10 <= 5) → False

# Exercise 2: Write Code
print(7 * 8)
print(15 > 10)
print(17 % 5)
print(3 ** 4)
print("hello" == "hello")

# Exercise 3: Shop Problem
# Your shop sells a product at ₹180, cost price is ₹167.

# Question - 1 - Calculate profit per unit

# Question - 2 - If customer buys 5 units, calculate total profit

# Question - 3 - Check if selling price is greater than cost price (True/False)

# Question - 4 - If you give 10% discount on selling price, what is new price?

# Question - 5 - Calculate profit at discounted price for 3 units

#1
sell_price = 180
cost_price = 167
profit = sell_price - cost_price
print(f"Profit per unit: {profit}")

#2
total_profit = profit * 5
print(f"Total profit for 5 units: {total_profit}")

#3
is_selling_price_greater = sell_price > cost_price
print(f"Is selling price greater than cost price? {is_selling_price_greater}")

#4
discount = 0.10
new_price = sell_price - (sell_price * discount)
print(f"New price after 10% discount: {new_price}")

#5
discounted_profit = new_price - cost_price
total_discounted_profit = discounted_profit * 3
print(f"Total profit for 3 units at discounted price: {total_discounted_profit}")

# Exercise 4: Fix the Error

# Wrong Code - 1 - print(5 + "3")

# Wrong Code - 2 - print(10 / 0)

# Wrong Code - 3 - print("Hello" == hello)

# Wrong Code - 4 - print(2 ** 3 ** 2) — What does this actually compute?

# Fixed Code - 1
print(5 + int("3"))

# Fixed Code - 2
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Fixed Code - 3
print("Hello" == "hello")

# Fixed Code - 4
print(2 ** (3 ** 2))