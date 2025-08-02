# Dictionary.py
# This script demonstrates the use of dictionaries in Python.
# Features:
# - Creating dictionaries
# - Accessing values
# - Adding and updating key-value pairs
# - Removing key-value pairs
# - Iterating over keys and values
# Examples included:

# creating a dictionary
student_scores = {
    "Alice": [85, 90, 95],
    "Bob": [78, 82, 88],
    "Charlie": [92, 88, 84]
}

fruits = {"apple": 1.2, "banana": 0.5, "cherry": 2.0}
name = {"name": "John", "age": 30, "city": "New York"}

#  dictionary are mutable data types

d = {"name": "Alice", "age": 25, "city": "Wonderland"}
d["age"] = 26  # updating value
d["country"] = "Fantasy"  # adding new key-value pair   
print("Updated dictionary:", d)

# unordered dictionary

student = {  
    "name": "Alice",
    "age": 20,
    "marks": [85, 90, 95],
    "is_graduated": False
}

print (student)

# index by keys

print ("Name:", student["name"])  # Accessing value by key

# no duplicate keys allowed

# keys must be immutable types (strings, numbers, tuples)



# 1 st method of creating a dictionary

# Empty dictionary
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# Dictionary with initial data
student1 = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}

# Dictionary with different data types
mixed_dict = {
    "string_key": "Hello",
    42: "Number key",
    (1, 2): "Tuple key",
    "boolean": True,
    "list": [1, 2, 3]
}

# 2nd method of creating a dictionary

# Using the dict() constructor

# From keyword arguments
person = dict(name="Bob", age=25, city="New York")

# From a list of tuples
coordinates = dict([("x", 10), ("y", 20), ("z", 30)])

# From another dictionary (creates a copy)
original = {"a": 1, "b": 2}
copy_dict = dict(original)

print(copy_dict)
print(original)

print("Person dictionary:", person)

# method no 3 dictionary comprehension

"""
square = {x: x**2 for x in range(1,6)}
range (1,6) generates numbers from 1 to 5
x:x**2 creates key-value pairs where the key is x and the value is x squared
print("Square dictionary:", square)
"""

square = {x: x**2 for x in range(1,6)}
print("Square dictionary:", square)

# example

name1 = {"alice", "bob", "charlie"}
ages = {25, 30, 35}
people = {name: age for name , age in zip(name1, ages)}
print("People dictionary:", people)

# accessing values

name2 = {"alice": 25, "bob": 30, "charlie": 35}
print("Alice's age:", name2["alice"])

# get (method to access values safely) 

qwerty = {
    "name": "Alice",
    "age": 25,
    "city": "Wonderland",
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}

# method 1
print (qwerty["name"])
# method 2 (using get)
print(qwerty.get("name"))  # Output: Alice
print(qwerty.get("age"))  # Output: 25
print(qwerty.get("country", "Not Found"))  # Output: Not Found (default value if key doesn't exist)
print(qwerty.get("city", "Not Found"))  # Output: Wonderland
print(qwerty.get("grade", "Not Found"))  # Output: A
print(qwerty.get("subjects", "Not Found"))  # Output: ['Math', 'Physics', 'Chemistry']
# method 3 nested values
print(qwerty["subjects"][0])  # Accessing first subject of Alice
print(qwerty.get("subjects", ["No subjects found"])[0])  # Accessing first subject with default value

"""
# try:
#     print(qwerty.get("subjects", ["No subjects found"])[0])  # Accessing fourth subject with default value
# except IndexError:
#     print("No fourth subject found")
"""

# Adding and updating key-value pairs

qwerty["hobby"] = "Reading"  # Adding a new key-value pair
qwerty["age"] = 26  # Updating an existing key-value pair
qwerty["subjects"].append("cs")  # Adding a new subject to the list
# qwerty["subjects"] = "English" # replacing the list with a string
# qwerty["subjects"].remove("Math","Chemistry")  # Removing a subject from the list
# update (method to update multiple key-value pairs)
qwerty.update({"city": "Wonderland", "grade": "A+"})  # Updating multiple key-value pairs
# qwerty.update({"Email": "iKu9a@example.com"})  # Adding a new key-value pair
qwerty.update(email = "iKu9a@example.com", phone = "1234567890")


print("Updated dictionary:", qwerty)