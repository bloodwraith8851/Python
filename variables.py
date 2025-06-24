# deep dive into variables and data types 
# why we use variables
# what data types are and why they matters
# How to use , check and convert data types

# Think of variable as a labeled containers. instead of writing the same data again and again we can store it in a variable and give it a name

# Rules for naming variables:
# 1. Variable names can only contain letters, numbers, and underscores.
# 2. Variable names cannot start with a number.
# 3. Variable names are case-sensitive.
# 4. Variable names cannot be a reserved keyword (like 'if', 'else', 'while', etc.).
# 5. Variable names should be descriptive and meaningful.
# 6. Variable names should not contain spaces.
# 7. Variable names should not use special characters (like @, #, $, %, etc.).
# 8. Variable names should be kept short but descriptive.

#example
name = "RAKESH" # string variable
age = 15 # integer variable
height = 5.9 # float variable
is_student = True # boolean variable

print("my name is", name)
print("my age is", age)
print("my height is", height)
print("am I a student?", is_student)

# Data types in Python
# 1. String: A sequence of characters enclosed in quotes (single or double).    
#    Example: "Hello", 'World'
# 2. Integer: A whole number without a decimal point.
#    Example: 10, -5, 0
# 3. Float: A number with a decimal point.
#    Example: 3.14, -2.5, 0.0
# 4. Boolean: A value that can be either True or False.
#    Example: True, False

# why this matters:
# 1. Understanding data types helps us choose the right type for our variables.
# 2. It allows us to perform operations on different data types.
# 3. It helps us avoid errors in our code.
# 4. It allows us to convert between different data types when necessary.
# 5. you cannot perform operations on incompatible data types (e.g., adding a string to an integer).

# Checking data types
# in python we can check the data type of a variable using the built-in type() function

# example

print("TYPE OF NAME",type(name))  # <class 'str'>
print("TYPE OF AGE",type(age))   # <class 'int'>
print("TYPE OF HEIGHT",type(height))  # <class 'float'>
print("TYPE OF IS_STUDENT",type(is_student))  # <class 'bool'>

# Converting data types
# in python we can convert data types using built-in functions
# 1. str(): Converts a value to a string.
# 2. int(): Converts a value to an integer.
# 3. float(): Converts a value to a float.
# 4. bool(): Converts a value to a boolean.

# example

# string - integer conversion
num_str = "123"
num_int = int(num_str) # Converts string to integer
print(num_int + 10)  # Output: 133

# print(int(num_str)+ 10) # Output: 133 # one line code

# string - float conversion
num_float_str = "3.14"  
num_float = float(num_float_str) # Converts string to float
print(num_float + 1.0)  # Output: 4.14

# print(float(num_float_str) + 1.0)  # Output: 4.14 # one line code

# integer - string conversion

num_int_str = 456
num_str_from_int = str(num_int_str)  # Converts integer to string
print(num_str_from_int + " is a number")  # Output: 456 is a number

# print(str(num_int_str) + " is a number")  # Output: 456 is a number # one line code

# float - string conversion

num_float_str = 7.89
num_str_from_float = str(num_float_str)  # Converts float to string
print(num_str_from_float + " is a float")  # Output: 7.89

# print(str(num_float_str) + " is a float")  # Output: 7.89 # one line code

# boolean - string conversion

is_true = True
is_true_str = str(is_true)  # Converts boolean to string
print(is_true_str + " is a boolean")  # Output: True is a boolean

# print(str(is_true) + " is a boolean")  # Output: True is a boolean # one line code

# boolean - integer conversion
is_false = False
is_false_int = int(is_false)  # Converts boolean to integer (False = 0
# True = 1)
print(is_false_int + 5)  # Output: 5
# print(int(is_false) + 5)  # Output: 5 # one line code 

# boolean - float conversion
is_true_float = float(is_true)  # Converts boolean to float (True = 1
# False = 0.0)
print(is_true_float + 2.0)  # Output: 3.0

# print(float(is_true) + 2.0)  # Output: 3.0 # one line code