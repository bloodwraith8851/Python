## topics

# - arithmetic operators
# - order of operations
# - integer and floats
# - math module
# - simple calculator

## arithmetic operators

# In Python, arithmetic operators are used to perform mathematical operations on numeric values.
# The basic arithmetic operators in Python are:

# + additions
# - subtraction
# * multiplication
# / division
# % modulus (remainder of division) for example 7 % 3 = 2
# ** exponentiation (power) 2** 3 = 8
# // floor division (division that rounds down to the nearest whole number) for example 7/2 = 3.5 (/) floor division = 7//2 = 3

# Example of arithmetic operators
a = 10
b = 3

# Addition
addition = a + b
print(f"Addition: {a} + {b} = {addition}")
# print("addition: 10 + 3 = ", 10 + 3)  # Output: addition: 13

# Subtraction
subtraction = a - b
print(f"Subtraction: {a} - {b} = {subtraction}")
# print("subtraction: 10 - 3 = ", 10 - 3)  # Output: subtraction: 7

# Multiplication
multiplication = a * b
print(f"Multiplication: {a} * {b} = {multiplication}")
# print("multiplication: 10 * 3 = ", 10 * 3)  # Output: multiplication: 30

# Division
division = a / b        
print(f"Division: {a} / {b} = {division}")
# print("division: 10 / 3 = ", 10 / 3)  # Output: division: 3.3333333333333335

# Modulus
modulus = a % b
print(f"Modulus: {a} % {b} = {modulus}")
# print("modulus: 10 % 3 = ", 10 % 3)  # Output: modulus: 1

# Exponentiation
exponentiation = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation}")
# print("exponentiation: 10 ** 3 = ", 10 ** 3)  # Output: exponentiation: 1000

# Floor Division
floor_division = a // b 
print(f"Floor Division: {a} // {b} = {floor_division}")
# print("floor division: 10 // 3 = ", 10 // 3)  # Output: floor division: 3

# order of operations
# In Python, the order of operations follows the standard mathematical rules, often remembered by the acronym
# bodmas (Brackets, Orders, Division and Multiplication, Addition and Subtraction).

print(2 + 3 * 4) # Output: 14 (Multiplication before Addition)
print((2 + 3) * 4) # Output: 20 (Brackets first)

# pemdas
# In Python, the order of operations follows the PEMDAS rule:   
# Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

print(2 + 3 * 4)  # Output: 14 (Multiplication before Addition)
print((2 + 3) * 4)  # Output: 20 (Parentheses first)

# integer and floats
# In Python, integers are whole numbers without a decimal point, while floats are numbers with a decimal point.
# Example of integers and floats
int_num = 10  # Integer
float_num = 3.14  # Float
print(f"Integer: {int_num}, Float: {float_num}")
# Arithmetic operations with integers and floats
sum_result = int_num + float_num
print(f"Sum: {int_num} + {float_num} = {sum_result}")
# Difference: {int_num} - {float_num} = {int_num - float_num}")
diff_result = int_num - float_num
print(f"Difference: {int_num} - {float_num} = {diff_result}")
# Product: {int_num} * {float_num} = {int_num * float_num}")
prod_result = int_num * float_num
print(f"Product: {int_num} * {float_num} = {prod_result}")
# Quotient: {int_num} / {float_num} = {int_num / float_num}")
quotient_result = int_num / float_num
print(f"Quotient: {int_num} / {float_num} = {quotient_result}")
# Modulus: {int_num} % {float_num} = {int_num % float_num}")
modulus_result = int_num % float_num
print(f"Modulus: {int_num} % {float_num} = {modulus_result}")
# Exponentiation: {int_num} ** {float_num} = {int_num ** float_num}")
exponentiation_result = int_num ** float_num
print(f"Exponentiation: {int_num} ** {float_num} = {exponentiation_result}")
# Floor Division: {int_num} // {float_num} = {int_num // float_num}")
floor_division_result = int_num // float_num
print(f"Floor Division: {int_num} // {float_num} = {floor_division_result}")

# math module
# The math module in Python provides mathematical functions and constants.
# math.sqrt() is used to calculate the square root of a number.
# math.pi is a constant representing the value of pi (π).
# math.e is a constant representing the base of natural logarithms (e).
# math.factorial() is used to calculate the factorial of a number.
# math.floor() is used to round a number down to the nearest integer.
# math.ceil() is used to round a number up to the nearest integer.
# math.log() is used to calculate the natural logarithm of a number.
# math.log10() is used to calculate the base-10 logarithm of a number.
# math.log2() is used to calculate the base-2 logarithm of a number.
# math.sin() is used to calculate the sine of a number.
# math.cos() is used to calculate the cosine of a number.
# math.tan() is used to calculate the tangent of a number.
# math.sinh() is used to calculate the hyperbolic sine of a number.
# math.cosh() is used to calculate the hyperbolic cosine of a number.
# math.tanh() is used to calculate the hyperbolic tangent of a number.
# math.asin() is used to calculate the arcsine of a number.
# math.acos() is used to calculate the arccosine of a number.
# math.atan() is used to calculate the arctangent of a number.
# math.sinh() is used to calculate the hyperbolic sine of a number.
# math.cosh() is used to calculate the hyperbolic cosine of a number.
# math.tanh() is used to calculate the hyperbolic tangent of a number.
# math.asinh() is used to calculate the inverse hyperbolic sine of a number.
# math.acosh() is used to calculate the inverse hyperbolic cosine of a number.
# math.atanh() is used to calculate the inverse hyperbolic tangent of a number.
# math.hypot() is used to calculate the Euclidean norm (magnitude) of a vector.
# math.isclose() is used to check if two numbers are close to each other.
# math.comb() is used to calculate the number of combinations.
# math.perm() is used to calculate the number of permutations.
# math.prod() is used to calculate the product of a sequence of numbers.
# math.gcd() is used to calculate the greatest common divisor (GCD) of two or more numbers.
# math.lcm() is used to calculate the least common multiple (LCM) of two or more numbers.
# math.remainder() is used to calculate the remainder of a division.
# math.copysign() is used to copy the sign of one number to another number.
# math.fabs() is used to calculate the absolute value of a number.
# math.degrees() is used to convert radians to degrees.
# math.radians() is used to convert degrees to radians.
# math.trunc() is used to truncate a number to its integer part.
# math.dist() is used to calculate the Euclidean distance between two points in space.
# math.isfinite() is used to check if a number is finite (not infinity or NaN).
# math.isinf() is used to check if a number is infinite.
# math.isnan() is used to check if a number is not a number (NaN).
# math.isqrt() is used to calculate the integer square root of a number.
# math.acos() is used to calculate the arccosine of a number.

import math

# Example of using the math module
print("square root of 15:", math.sqrt(15)) # Output: square root of 15: 3.872983346207417
print("value of pi:", math.pi) # Output: value of pi: 3.141592653589793
print("value of e:", math.e) # Output: value of e: 2.718281828459045
print("factorial of 5:", math.factorial(5)) # Output: factorial of 5: 120
print("floor of 3.7:", math.floor(3.7)) # Output: floor of 3.7: 3
print("ceil of 3.7:", math.ceil(3.7)) # Output: ceil of 3.7: 4
print("logarithm of 10:", math.log(10)) # Output: logarithm of 10: 2.302585092994046
print("logarithm base 10 of 100:", math.log10(100)) # Output: logarithm base 10 of 100: 2.0
print("logarithm base 2 of 8:", math.log2(8)) # Output: logarithm base 2 of 8: 3.0
print("sine of 30 degrees:", math.sin(math.radians(30))) # Output: sine of 30 degrees: 0.49999999999999994
print("cosine of 60 degrees:", math.cos(math.radians(60))) # Output: cosine of 60 degrees: 0.5000000000000001
print("tangent of 45 degrees:", math.tan(math.radians(45))) #   # Output: tangent of 45 degrees: 0.9999999999999999
print("hyperbolic sine of 1:", math.sinh(1)) # Output: hyperbolic sine of 1: 1.1752011936438014
print("hyperbolic cosine of 1:", math.cosh(1)) # Output:    # hyperbolic cosine of 1: 1.5430806348152437
print("hyperbolic tangent of 1:", math.tanh(1)) # Output:   # hyperbolic tangent of 1: 0.7615941559557649
print("arcsine of 0.5:", math.asin(0.5))    # Output: arcsine of 0.5: 0.5235987755982989

# simple calculator
# A simple calculator can be implemented using Python's arithmetic operators and input functions.
# The input function is used to get user input from the command line. 
# The eval function is used to evaluate a string as a Python expression.

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