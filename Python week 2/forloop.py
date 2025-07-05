# for loop

"""A for loop in python repeats a block of code for each item in a sequence"""
"""sequence can be a list, tuple, string, range, dictionary, set, or any other iterable object"""
"""fixed number of iterations"""

#syntax

"""
for iteam in sequence:
    # code to repeat
"""

# The range function

"""
The range function returns a sequence of numbers
The range function takes two arguments: start and stop
The range function returns a sequence of numbers from start to stop-1
"""

# range(5) -> 0, 1, 2, 3, 4
# range(start,stop) -> start, start+1, start+2, start+3, start+4
# range(2,6) -> 2, 3, 4, 5
# range(start,stop,step) -> start, start+step, start+step*2, start+step*3, start+step*4

"""
start -> start value -> start counting from 1 by default
stop -> stop value -> stop counting before this value
step -> counting step -> default is 2 (skip every other number)
"""
# range (1,11,2) -> 1, 3, 5, 7, 9

#example
for i in range(1):
    print(i)
for u in range(1,11):
    print(u)
for o in range(1,11,2):
    print(o)

# iterating over a string

"""
you can loop through a string using a for loop
"""

for letter in "hello":
    print(letter) # Output: h e l l o

# Multiplication table genrator 

num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num * i}")

# print even numbers

for i in range(2,21,2):
    print(i)