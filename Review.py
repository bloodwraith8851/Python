# week 1 recap

"""Topics covered in week 1:"""

# - Day 1: print(),python intro,syntax
# - Day 2: variables,datatypes,conversion
# - Day 3: strings and formatting
# - Day 4: math opetators,math module
# - Day 5: input and type casting
# - Day 6: comments,docstrings
# - Day 7: review and practice

"""Mini Projects:"""

#  - personal info collector

print("Welcome to the Personal Info Collector!\n")  # print a welcome message

name = input("Please enter your name: ")  # take name input from the user
age = int(input("Please enter your age: "))  # take age input from the user
email = input("Please enter your email: ")  # take email input from the user
phone = input("Please enter your phone number: ")  # take phone number input from the user
address = input("Please enter your address: ")  # take address input from the user

print ("\n ------------ Personal Information Summary ------------\n")  # print a summary header
print(f"Name: {name}")  # print the name
print(f"Age: {age}")  # print the age
print(f"Email: {email}")  # print the email
print(f"Phone Number: {phone}")  # print the phone number   
print(f"Address: {address}")  # print the address  

# Age checker

age = int(input("Please enter your age: "))  # take age input from the user
if age >= 18:
    print("you are eligible to vote.")  # print a message if the user is eligible to vote
else:
    print("you are not eligible to vote.")  # print a message if the user is not eligible to vote

# Temperature converter

celsius = float(input("Please enter the temperature in Celsius: "))  # take temperature input in Celsius

fahrenheit = (celsius * 9/5) + 32 # convert Celsius to Fahrenheit

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# simple interest calculator

principal = float(input("Please enter the principal amount: "))  # take principal amount input from the user
rate = float(input("Please enter the rate of interest: "))  # take rate of interest input from the user
time = float(input("Please enter the time in years: "))  # take time input from the user

intrest = (principal * rate * time)/100  # calculate simple interest

print(f"The simple interest for a principal amount of {principal}, rate of interest {rate}%, and time {time} years is: {intrest}")  # print the calculated simple interest

# word counter

sentence = input("Please enter a sentence: ")  # take sentence input from the user
words = sentence.split()  # split the sentence into words
word_count = len(words) # count the number of words

print(f"The number of words in the sentence is: {word_count}")  # print the word count

# multiplication table generator

num = int(input("Please enter a number to generate its multiplication table: "))  # take number input from the user
for i in range(1, 11) :  # loop through numbers 1 to 10
    print(f"{num} x {i} = {num * i}")  # print the multiplication table for the given number

# simple calculator

num1 = float(input("Enter first number: "))  # Input first number
num2 = float(input("Enter second number: "))  # Input second number
operation = input ("Enter operation (+, -, *, /, %, **, //): ")  # Input operation

if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")  # Output result
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")  # Output result
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")  # Output result
elif operation == '/':
    print(f"{num1} / {num2} = {num1 / num2}")  # Output result
elif operation == '%':
    print(f"{num1} % {num2} = {num1 % num2}")  # Output result
elif operation == '**': 
    print(f"{num1} ** {num2} = {num1 ** num2}")  # Output result
elif operation == '//':
    print(f"{num1} // {num2} = {num1 // num2}")  # Output result
else:
    print("Invalid operation")