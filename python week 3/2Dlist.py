# 2d list 

"""
a 2d list is a list of lists. think of it like a table ,where each row is a list and you have multiple such rows
"""
# syntax :
"""
2d_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""

# each elements can be acessed using two index : list[row_index][column_index]

# creating a 2d list

list = [
    [1, 2, 3],  # first row
    [4, 5, 6],  # second row    
    [7, 8, 9]   # third row
]

# accessing elements in a 2d list

# print(list[0])  # Output: [1, 2, 3] (first row)
# print(list[1])  # Output: [4, 5, 6] (second row)
# print(list[2])  # Output: [7, 8, 9] (third row)
# print(list[0][0])  # Output: 1 (first row, first column element)
# print(list[1][2])  # Output: 6 (second row, third column element)

# iterating through a 2d list

# method 1 : using nested for loop

# for row in list:  # iterating through each row
#     for item in row:  # iterating through each item in the row
#         print(item)  # printing each item


kitchen = [
    ["biscuits", "bread", "milk"],
    ["eggs", "cheese", "butter"],
    ["salt", "pepper", "sugar"]
]

# for shelf in kitchen: # outer loop checking each shelf
#     # print (shelf) # printing each shelf
#     # print("Shelf items:")  # printing shelf header
#     for item in shelf: # inner loop checking each item in the shelf
#         print(f"Mila: {item}")  # printing each item in the kitchen shelves

# method 2 : using indices (index ka plural is indices)

for i in range(len(list)):  # iterating through the indices of the outer list
    print(list[i]) # printing each row using indices
    for j in range(len(list[i])):  # iterating through the indices of the inner lists
        print(list[i][j])  # printing each item using indices