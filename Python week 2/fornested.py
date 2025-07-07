# what are nested loops?
"""
A nested loop is a loop inside another loop.
The inner loop is executed first, then the outer loop is executed. 
"""

# Syntax

"""
for iteam1 in sequence1:
    for iteam2 in sequence2:
        # code to repeat
"""

# pattern printing with nested loop

"""
pattern printing is a common use case for nested loop. you can print triangle patterns, square paters or any other pattern using nested loops
"""

# end = "\n" # this is used to print in a new line
# end = " " #space after print
# end = "" # no space continuous text
# end = "...." # adds dot after print

#example

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

for i in range (1,5):    # outer loop runs 5 times for rows
    for j in range(i): # inner loop runs 1 time for each row
      print("*",end="") #print stars in same line
    print() # move to next line

