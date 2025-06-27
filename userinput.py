# what is input()

# Input function in Python is used to take input from the user. It reads a line from input, converts it into a string, and returns it.

#example
name = input("enter your name:")   # user input
print("Hello", name) # Output: Hello <name>

# convert input to integer
# since input() returns a string, we can convert it to an integer using int() function.

age = int(input("Enter your age:")) # user input
print("You are", age, "years old")  # Output: You are <age

num1 = int(input("Enter first number: "))  # Input first number
num2 = int(input("Enter second number: "))  # Input second number
operation = input("Enter operation (+, -, *, /, %, **, //): ")  # Input operation
if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")  # Output result
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    print(f"{num1} / {num2} = {num1 / num2}")   # Output result
elif operation == '%':
    print(f"{num1} % {num2} = {num1 % num2}")   # Output result
elif operation == '**': 
    print(f"{num1} ** {num2} = {num1 ** num2}")  # Output result
elif operation == '//':
    print(f"{num1} // {num2} = {num1 // num2}")  # Output result
else:
    print("Invalid operation")

# formatting output

#concatenation:

print("hello" + " world")  # Output: hello world

# using f-strings for formatting

name = "Alice"
print (f"hello {name}")  # Output: hello Alice


# using format() method for formatting

print("Hello {}".format(name))  # Output: Hello, Alice


# full intrective example

name1 = input("Enter your name: ")  # user input
age = int(input("Enter your age: "))  # user input
color = input("Enter your favorite color: ")  # user input
print(f"Hello {name1} , you are {age} years old and your favorite color is {color}.")  # Output: Hello <name1>, you are <age> years old and your favorite color is <color>.

# common mistakes in user input

# typing errors: "age" + 20 (can,t concatenate string and integer)
# not using input before using math functions:
# forgetting to convert input to the correct type (e.g., using int() for integers)
# misspelled variable names (e.g., using "age" instead of "Age")