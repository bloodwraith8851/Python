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

# Removing key-value pairs

del qwerty["city"]  # Removing a key-value pair
qwerty.pop("grade")  # Removing a key-value pair
iteam = qwerty.popitem()  # Removing the last key-value pair
# qwerty.clear()  # Removing all key-value pairs
print ("Removed item:", iteam)
# print("Updated dictionary:", qwerty)
print("Dictionary after clearing:", qwerty)

# dictionary methods

nidhi = {
    "name": "Nidhi",
    "age": 17,
    "city": "vadodara",
    "hobby": "reading",
    "subjects": ["Math", "Physics", "Chemistry"],
    "grade": "-X"
}

# keys () - returns all keys in the dictionary
print ("Keys:",nidhi.keys())
print ("keys as list:", list(nidhi.keys()))

# values () - returns all values in the dictionary
print ("Values:",nidhi.values())
print ("values as list:", list(nidhi.values()))

# items() - returns key-value pairs as tuples
print("Items:", nidhi.items())
print("Items as list:", list(nidhi.items()))

# len() - returns the number of key-value pairs in the dictionary
print("Number of key-value pairs:", len(nidhi))

# in operator - checks if a key exists in the dictionary

print ("name" in nidhi)
print("age" in nidhi)
print("country" in nidhi)  # False, as 'country' is not a key in the dictionary

# copy() - creates a shallow copy of the dictionary
nidhi_copy = nidhi.copy()
print("Copied dictionary:", nidhi_copy)

# advance dictionary methods

# setdefault() - returns the value of a key if it exists, otherwise sets it to a default value

nidhi.setdefault("country", "India")  # Sets 'country' to 'India' if it doesn't exist
print("After setdefault:", nidhi)

nidhi.setdefault("grade", "A") # Sets 'grade' to 'A' if it doesn't exist
print("After setdefault for existing key:", nidhi)

# fromkeys() - creates a new dictionary with specified keys and a default value

subjects = ["Math", "Physics", "Chemistry"]
scores = dict.fromkeys(subjects, 0)  # Creates a dictionary with subjects as keys and 0 as default value
scores["Math"] = 95  # Updating the score for Math
scores["Physics"] = 90  # Updating the score for Physics
scores["Chemistry"] = 85  # Updating the score for Chemistry    
print("Scores dictionary from keys:", scores)

# merging dictionaries (python 3.9+ feature)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1|dict2  # Merging dictionaries using the | operator
print("Merged dictionary:", merged)

# nested dictionary

school ={
    "students" : {
        "Alice": {"age": 20, "grade": "A"},
        "Bob": {"age": 22, "grade": "B"},
        "Charlie": {"age": 21, "grade": "C"}
    },
    "teachers": {
        "Mr. Smith": {"subject": "Math", "experience": 5},
        "Ms. Johnson": {"subject": "Physics", "experience": 3}
    }
}

print ("School dictionary:", school)
# Accessing nested dictionary values
print(school["students"]["Alice"]["grade"])  # Output: A
print(school["teachers"]["Mr. Smith"]["subject"])  # Output: Math

# error handling with dictionaries

def safe_get_grade(students,name):
    """Safely get the grade of a student by name."""
    try:
        return students[name]["grade"]
    except KeyError:
        return "Student not found"
    except TypeError:
        return "Invalid data structure"
    
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "pagal": ["not a dict"],
    "Charlie": {"age": 21, "grade": "C"}
}

print(safe_get_grade(students, "Alice"))  # Output: A
print(safe_get_grade(students, "David")) # Output: Student not found
print(safe_get_grade(students, "pagal"))  # Output: Invalid data structure

grades = {
    "Math": 85,
    "Science": 90,
    "English": 88
}

iteams = grades.items()  # Getting key-value pairs as tuples
sorted1 = sorted(grades.items())  # Sorting by values in descending order

print ("Grades items:", iteams)
print("Sorted grades:", sorted1)