# if statement

"""
an if statement is a conditional statement that allows you to execute a block of code if a certain condition is true.
The syntax of an if statement in Python is as follows:
"""

# basic if statement

"""
 syntax:
 if condition:
    # code to execute if condition is true
"""

#example

# age = 17
# if age >= 18:
#     print("You are eligible to vote.")

# if-else statement

"""
syntax:
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
"""

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# if-elif-else statement

# used when you want to check multiple conditions

"""
syntax:
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if neither condition1 nor condition2 is true
"""

#example

# marks = 85
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# nested if statement

"""
syntax:
if condition1:
    # code to execute if condition1 is true
    if condition2:
        # code to execute if condition2 is true
    else:
        # code to execute if condition2 is false
else:
    # code to execute if condition1 is false
"""

#example

age1 = 20
has_id = False
if age1 >= 18 :
    if has_id:
        print("You are eligible to vote.")
    else:
        print("You need valid ID to vote.")
else:
    print("you need to be 18 or older to vote. and you need to have a valid ID.")

# indentation matter

# indentation is the space at the beginning of a line that indicates the level of nesting or indentation of the code

# example

# if age >= 18:
#     if has_id:
#         print("You are eligible to vote.")
#     else:
#         print("You need valid ID to vote.")
# else:
#     print("you need to be 18 or older to vote. and you need to have a valid ID.")

# common mistakes

"""
forgetting colons
forgetting indentation
writing else instead of elif
writing elif instead of else
writing if x = 5 instead of if x == 5 (use == for comparison)
"""