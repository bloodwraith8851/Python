# list comprehensions

"""
a list comprehension is a way to create a new list based on the elements of an existing list
"""

# regular way

squares =[]
for i in range(5):
    squares.append(i*i)
print(squares) # [0, 1, 4, 9, 16]

# list comprehension way (cool way):

squares = [i*i for i in range(5)]
print(squares) # [0, 1, 4, 9, 16]

# list comprehension with conditions

squares = [i*i for i in range(5) if i % 2 == 0]
print(squares) # [0, 4, 16]

# example 

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if f.endswith("y")]
print(friend) # ['Bobby', 'jerry']

# example 2

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if f.startswith("T")]
print(friend) # ['Tommy']

# example 3

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if f.startswith("T") and f.endswith("y")]
print(friend)

# example 4

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if f.startswith("T") or f.startswith("j")]
print(friend)

# example 5

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if not f.startswith("T")]
print(friend)

# example 6

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if not f.startswith("T") and not f.startswith("j")]
print(friend)

# example 7

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if not f.startswith("T") or not f.startswith("j")]
print(friend)

# example 8

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if not f.startswith(("T","j"))]
print(friend) # ['Ricky', 'Bobby', 'sam']

# example 9

friends = ["Ricky","Bobby","sam","Tommy","jerry","joe"]
friend = [f for f in friends if f.startswith(("T","j"))]
print(friend) # ['Tommy', 'jerry']
