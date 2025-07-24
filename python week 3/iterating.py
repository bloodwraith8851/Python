# iterating through lists
# This script demonstrates various ways to iterate through lists in Python.
# Features:
# - Explains the concept of iteration.
# - Shows basic iteration over a list using a for loop.
# - Demonstrates the use of the enumerate() function to access both index and value during iteration.
# - Illustrates how to start enumeration from a custom index.
# - Explains the use of the range() function for generating sequences in loops.
# - Provides an example of modifying list elements during iteration using enumerate().
# Examples included:
# - Printing each item in a list.
# - Printing each item with its index.
# - Modifying elements of a list in-place.
# Intended for beginners learning about iteration and list manipulation in Python.

# What is iteration?

"""
Iteration is the process of going through each item in a collection (like a list or tuple) one by one.
"""

# Example of iterating through a list

example = ["apple", "banana", "cherry"]
for iteam in example: # iterating through the list example and printing each iteam
    print(iteam)

# enumerate function
"""
The enumerate function adds a counter to an iterable and returns it as an enumerate object. 
This is useful when you need both the index and the value of each item in a list.
"""
# Example of using enumerate

example = ["apple", "banana", "cherry"]
for index,iteam in enumerate(example): # iterating through the list example and printing each iteam with its index
    print(f"Index: {index}, Item: {iteam}") # Output: Index: 0, Item: apple

for index, iteam in enumerate(example, start=1): # starting the index from 1
    print(f"Index: {index}, Item: {iteam}") # Output: Index: 1, Item: apple

# Using range function
"""
The range function generates a sequence of numbers, which is often used in loops to iterate a specific number of times.
"""
# Example of using range

for i, iteam in enumerate(example): # iterating through the list example and printing each iteam with its index
    print(f"Index: {i}, Iteam: {iteam}") # Output: Index: 0, Item: apple

marks = [85, 90, 78, 92, 88]
for i, mark in enumerate(marks):
    marks[i] = mark + 5  # Adding 5 to each mark
print(marks)  # Output: [90, 95, 83, 97, 93]

#zip function

"""
The zip function combines two or more iterables (like lists) into tuples, pairing elements from each iterable together.
"""

name = ["Alice", "Bob", "Charlie", "David"]
marks = [85, 90, 78]
for name, mark in zip(name, marks):
    print(f"{name} scored {mark}")  # Output: Alice scored 85, Bob scored 90, Charlie scored 78
