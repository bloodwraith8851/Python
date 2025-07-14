# list methods and operations

# common list methods

# append() - adds an iteam to the end of the list # done in previous class
# clear() - removes all iteams from the list # done in previous class
# copy() - returns a copy of the list
# count() - returns the number of times an iteam appears in the list
# extend() - adds the elements of a list to the end of the current list 
# index() - returns the index of the first occurrence of an iteam in the list # done in previous class
# insert() - inserts an iteam at a specific index in the list # done in previous class
# pop() - removes the last iteam from the list and returns it  # done in previous class
# remove() - removes the first occurrence of an iteam from the list # done in previous class
# reverse() - reverses the order of the iteams in the list 
# sort() - sorts the iteams in the list

# list operations

# len() - returns the length of the list
# max() - returns the largest iteam in the list
# min() - returns the smallest iteam in the list
# sum() - returns the sum of the iteams in the list

# sort

# list.sort() - sorts the iteams in the list
# list.sort(reverse=True) - sorts the iteams in the list in reverse order

# example

"""list.sort()"""

example = ["banana", "apple", "cherry"]
example.sort()
print(example)

"""list.sort(reverse=True)"""

example.sort(reverse=True)
print(example)

# reverse

"""list.reverse()"""

numbers = [2, 1, 5, 4, 3]
numbers.reverse()
print(numbers)

# example = ["banana", "apple", "cherry"]
# example.reverse()
# print(example)

# count

"""list.count()"""

example = ["banana", "apple", "cherry", "banana", "apple"]
count = example.count("banana")
print(count)

# index

"""list.index()"""

example = ["banana", "apple", "cherry"]
index = example.index("apple")
print(index)

# copy

"""list.copy()"""

example = ["banana", "apple", "cherry"]
copy = example.copy()
print(copy) # ['banana', 'apple', 'cherry']

# extend

"""list.extend()"""

example = ["banana", "apple", "cherry"]
example.extend(["orange", "grape"])
print(example)

# sum

"""list.sum()"""

example = [1, 2, 3, 4, 5]
sum = sum(example)
print(sum)

# example = ["banana", "apple", "cherry"]
# sum = sum(example)   
# print(sum)

# len

"""list.len()"""

example = ["banana", "apple", "cherry"]
length = len(example)
print(length)

# max

"""list.max()"""

example = [1, 2, 3, 4, 5]
maximum = max(example)
print(maximum)

# min

"""list.min()"""

example = [1, 2, 3, 4, 5]
minimum = min(example)
print(minimum)

