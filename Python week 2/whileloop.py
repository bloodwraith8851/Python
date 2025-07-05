# while loop
"""A while loop in python repeats a block of code as long as given condition is true"""
# syntax
"""
while condition:
    # code to repeat
"""

# example 

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# loop comnditions

"""The loop will continue to run as long as the condition is true"""
# example

x = 0
while x < 10:
    print("hi")
    x += 1

# infinty loops and how to avoid them

""" an infinity loop happens when the condition is always true and the loop never ends"""

# example

e = 5
while e < 0:
    print("oops")

# example

while True:
    print("\n1. say Hello\n2. say Bye\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Hello")
    elif choice == 2:
        print("Bye")
    elif choice == 3:
        print("Goodbye")
        break
    else:
        print("Invalid choice")

#sesor monitoring system

import random
import time
def read_sensor():
    number = random.randint(80,120)
    print(number)
    return number

while True:
    temprature = read_sensor()
    if temprature > 100:
        print("Alert Temprature is too high!")
    else:
        print("Temp is normal.")
    time.sleep(3)

# Break and continue statements

"""
break statement is used to exit the loop
continue statement is used to skip the current iteration of the loop
"""

# example

family = ["Dad","Mom","You","sister","baby brother"]
sick_today = ["Dad","baby brother"] # this is a list of family members who are sick today

for person in family:
    if person in sick_today:
        print(f"{person} is sick today.")
        continue
    print(f"{person} is not sick today.")

# example

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "absent"},
    {"name": "Diana", "grade": "D"},
    {"name": "Eve", "grade": "E"},
]

print(students[0]["name"])

for student in students:
    grade = student["grade"]
    if grade == "absent" or grade == "E":
        print (f"Skipping {student['name']} (reason: {'absent' if grade == 'absent' else 'E'})")
        continue
    print(f"{student['name']} has a grade of {student['grade']}")