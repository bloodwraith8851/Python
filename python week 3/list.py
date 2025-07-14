# introduction to list 

"""
a list is a collection of iteams in a particular order. lists allow you to stor multiple values in a single variable 
list are mutables
"""
#example 

example = ["apple", "banana", "cherry"]
# print(example)

# indexing and slicing

"""
you can acess list elements by their index (starting from 0)
"""
print(example[0]) # indexing
print(example[1:3]) # slicing

# adding elements

"""
-append(iteam) - adds an iteam to the end of the list
-insert(index, iteam) - inserts an iteam at a specific index in the list
"""

example.append("orange") # adding an iteam to the end of the list
example.insert(1, "mango") # inserting an iteam at a specific index in the list
# print(example)

# removing elements

"""
-remove(iteam) - quickly removes an iteam from the list
-pop(index) - removes an iteam from a specific index in the list
-del(list) - removes the entire list
"""
example.remove("banana") # removing an iteam from the list
example.pop(1) # removing an iteam from a specific index in the list
print(example)
del example #   removing the entire list

