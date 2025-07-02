# conditional expression

"""
A conditional expression is a short form of an if-else statement.
The syntax of a conditional expression in Python is as follows:
"""

# example

age = 18
status = "adult" if age >= 18 else "minor"
print(status)

# if- else expression

"""
if condition:
    expression1
else:
    expression2
"""

# conditional expression

"""
marks = 75
grade = "pass" if marks >= 50 else "fail"
"""

# key difference between if-else and conditional expression
# if-else statement can have multiple conditions
# conditional expression can only have one condition
# if-else used for complex conditions
# conditional expression used for simple conditions
# readability of if-else is better than conditional expression
# performance of if-else is better than conditional expression

# complex boolean expression

"""
you can combine multiple boolean expressions using logical operators (and, or, not)
to create a complex boolean expression
"""
marks = 75
if marks >= 50 and marks <= 100:
    print("pass")
else:
    print("fail")

# short-circuit evaluation

"""
logical operators (and, or, not) have short-circuit evaluation
this means that the second expression is not evaluated if the first expression is true
"""

# example

username = "admin"
password = "admin123"
if username == "admin1234" and password == "admin123":
    print("Access granted.")
else:
    print("Access denied.")

# now suppose 

"""
username = "admin1234"
password = "admin123"
"""
# the first condition username == "admin1234" is false
# py see its using and so even if the second condition password == "admin123" is true it dosen,t matter
# so py skips checking password == "admin123" this is short circuit
# so the program will print "Access denied."

# Real example - grade calculation

marks = int(input("Enter your marks: "))
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "E"
print(f"Your grade is {grade}")