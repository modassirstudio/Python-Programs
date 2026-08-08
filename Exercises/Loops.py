# Exercise 1: Predict Output
# 1.
for i in range(3): 
    print(i)
# It will print: 0, 1, 2

# 2.	
for i in range(1, 4): 
    print(i)	
# It will print: 1, 2, 3

# 3.	
for i in range(2, 11, 3): 
    print(i)
# It will print: 2, 5, 8, 11

# 4.	
x = 0; 
while x < 3: 
    print(x); x += 1
# It will print: 0, 1, 2

# Exercise 2: Write Code
# 1.	Print numbers 1 to 10 using for loop
for i in range(1, 11):
    print(i)

# 2.	Print even numbers from 2 to 20	
for i in range(2, 21, 2):
    print(i)

# 3.	Print "Hello" 5 times using while loop	
x = 0
while x < 5:
    print("Hello")
    x += 1

# 4.	Sum of numbers from 1 to 100	
total = 0
for i in range(1, 101):
    total += i
print(total)

# Exercise 3: Shop Loops
# 1.	You have 5 products. Print "Product [i]" for each.
for i in range(1, 6):
    print(f"Product {i}")

# 2.	Stock countdown: start at 10, print each number, stop at 0. Print "Out of Stock" at end.
x = 10
while x >= 0:
    print(x)
    x -= 1
print("Out of Stock")

# 3.	Given profits = [65, 240, 18, 300, 44], calculate total profit.
profits = [65, 240, 18, 300, 44]
total_profit = sum(profits)
print(total_profit)

# Exercise 4: Fix the Error
# 1.	for i in range(5) print(i)	
for i in range(5):
    print(i)

# 2.	while x < 5: print(x) x += 1	
x = 0
while x < 5:
    print(x)
    x += 1

# 3.	for i in range(5): print(i)
for i in range(5):
    print(i)