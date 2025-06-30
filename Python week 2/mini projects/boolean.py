# Even or odd checker 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Age verifier

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# password checker

password = input("Enter your password: ")
if password == "admin123":
    print("Access granted.")
elif password == "user123":
    print("Access granted.")
else:
    print("Access denied.")

# positive or negative number checker

n = int(input("Enter a number: "))
if n > 0:
    print(f"{n} is a positive number.")
elif n < 0:
    print(f"{n} is a negative number.")
else:
    print(f"{n} is zero.")

# Login system 

user = input("Enter your username: ")
pswd = input("Enter your password: ")

if user == "admin" and pswd == "password":
    print("Access granted.")
else:
    print("Access denied.")

# Two numbers comparator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is equal to {b}.")

# Teenager checker 

age = int(input("Enter your age: "))
# if 13 <= age <= 19:
if age >= 13 and age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")