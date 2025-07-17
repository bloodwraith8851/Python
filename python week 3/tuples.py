# What is a tuple?

"""
A tuple is like it can store multiple values. but  it's immutable. 
which means once you create it you can,t changew it and you can't add or remove iteam
"""

# example

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# tuple vs list:

"""
lists -> mutable -> can be changed (append,remove)
tuples -> immutable -> can't be changed 
tuples are faster and more memory efficient than lists
"""

# tuples methods

"""
count(value): returs how many times the value appears in the tuple
index(value): returns the index of the first occurrence of the value
"""

# example

nums = ("apple", "banana", "cherry", "apple")
print(nums.count("apple")) # 2
print(nums.index("cherry")) # 2

# when to use tuples

"""
when you dont want data to be changed
for fixed sets of values like coordinates,days of week,etc.
"""

# tuple unpacking example 

person = ("John", 25, "male")
name, age, gender = person
print(name) # John
print(age) # 25
print(gender) # male

# mini project 

coordinates = [(1, 2), (3, 4), (5, 6)]
for point in coordinates:
    x, y = point
    print(f"X: {x}, Y: {y}")
