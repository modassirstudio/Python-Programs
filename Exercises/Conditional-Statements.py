# Exercise 1: Predict the Output (What it will print?)
print(10 > 5)
# 10 is greater than 5, so it will print True.

print(10 == 10 and 5 > 3)	
# 10 equals 10 and 5 is greater than 3, so it will print True.

print(10 == 5 or 5 > 3)	
# 10 does not equal 5, but 5 is greater than 3, so it will print True.

print(not True)	
# True is negated, so it will print False.

print(5 != 5)	
# 5 does not equal 5, so it will print False cuz 5 is equals to 5.

# Exercise 2: Write Code
#1.	Check if age = 22 is 18 or above. Print "Adult" or "Minor".
age = 22
if age >= 18:
    print("Adult")
else:
    print("Minor")

#2.	Check if a number is positive, negative, or zero. Use if-elif-else.
number = 5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#3.	Print "Weekend" if day is Saturday or Sunday, else "Weekday".
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

#4.	Check if a person can vote (age >= 18 AND citizen = True).	
age = 20
citizen = True
if age >= 18 and citizen == True:
    print("Can vote")
else:
    print("Cannot vote")

# Exercise 3: Shop Logic
#1.	If stock > 0, print "Available". Else print "Out of Stock".
stock = 2
if stock > 0:
    print("Available")
else:
    print("Out of Stock")

#2.	If profit > 50 AND quantity > 5, print "Good Sale". Else print "Normal Sale".
profit = 60
quantity = 6
if profit > 50 and quantity > 5:
    print("Good Sale")
else:
    print("Normal Sale")

#3.	Give discount: If total > 5000, 10% discount. If total > 2000, 5% discount. Else no discount.
total = 6000
if total > 5000:
    print("10% discount")
elif total > 2000:
    print("5% discount")
else:
    print("No discount")


# Exercise 4: Fix the Error
#1.	if age > 18 print("Adult")
age = 20
if age > 18:
    print("Adult")

#2.	if name == "Modassir" print("Hello")	
name = "Modassir"
if name == "Modassir":
    print("Hello")

#3.	if 5 > 3 print("Yes") else print("No")
if 5 > 3:
    print("Yes")
else:
    print("No")