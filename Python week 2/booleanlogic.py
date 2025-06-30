#Boolean Values

""" 
Boolean values are either True or False
They are often used in conditional statements and loops
"""

# Example of boolean values
is_active = True
is_admin = False

# comparison operators
# Comparison operators return boolean values

"""
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
"""
# example of comparison operators

"""
5 > 3 is True
4 == 5 is False
"""

# Logical operators
# Logical operators are used to combine boolean values

# and : True if both operands are True
# or : True if at least one operand is True
# not : True if operand is False 

# example of logical operators

"""
True and False is False
True or False is True
not True is False
"""

# Truth tables

# A truth table is a table that shows the output of a logical operation for all possible input values

# AND operation truth table

"""
A | B | A and B
-----------------
T | T | T
T | F | F   
F | T | F
F | F | F
"""

# OR operation truth table

"""
A | B | A or B
-----------------
T | T | T 
T | F | T
F | T | T
F | F | F
"""

# NOT operation truth table
"""
A | not A
-----------------
T | F   
F | T
"""

# practicle examples

"""
10 > 5 and 3 < 1 # This will return False because 3 < 1 is False
7 != 2 or 4 == 4 # This will return True because 4 == 4 is True
not (6 <= 6) # This will return False because 6 <= 6 is True, and not True is False
(3 < 5) and not (2 > 1) # This will return false because 3 < 5 is True and not (2 > 1) is False
8 >= 8 or false  # This will return True because 8 >= 8 is True and false is False
"""