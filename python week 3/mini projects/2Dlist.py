students = [
    ["Alice", 85, 90, 78],
    ["Bob", 90, 85, 92],
    ["Charlie", 78, 88, 85],
    ["David", 92, 78, 90],
    ["Eve", 88, 92, 85],
    ["Frank", 80, 85, 88],
    ["Grace", 95, 90, 92],
    ["Hannah", 82, 88, 84],
    ["Ian", 87, 90, 85],
    ["Judy", 90, 92, 88],
    ["Kevin", 88, 85, 90],
    ["Linda", 85, 90, 92],
    ["Mike", 92, 88, 85],
    ["Nancy", 90, 85, 88]
]

for student in students:
    name = student[0]
    # print(f"Name: {name}")
    marks = student[1:]
    # print(f"Marks for {name}: {marks}")
    avg = sum(marks)/len(marks)
    print(f"Average marks for {name}: {avg:.2f}")

board = [
    ["X", "O", "X"],
    [" ", "X", " "],
    ["O", " ", "O"]
]

# for row in board:
#     print(" | ".join(row))  # Joining each row with a separator for better readability
#     print("-" * 9)  # Adding a separator line for clarity

for i, row in enumerate(board): #oye code bhaiya , board ke har row ko index ka sath ghumaooo
    # enumerate(board) means = mujha rows bih chaiye aur uska roll number(index) bhi chaiye
    # i hai row ka number (0,1,2) jaisa school mein attendance 
    # row mtlb current wali line - jaisa X O X YA O  O
    print(" | ".join(row)) # row ke sab iteam ko pipe laga ke line bana do jaisa sabji or roti 
    # join(row) means = list ke andar jo iteam hain unko ek string mein jod do 
    # "|" means = unko "|" se alag kar do jaisa sabji or roti ke beech mein thoda gap
    if i < len(board) -1: # agar yeh row last wali  nahi hai to ek line khech do uske neeche
        # len(board) = total kitni rows hain (3)
        # len(board) - 1 = index of last row (0-based index) (2)
        # i < 2 = sirf pehla do rows ke baad hi line ayegui 
        print("-" * 9)

# matrix addition

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],  
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [] # ek khali box banya jisme final answer jayega

for i in range(3): # outer loop (i) matlab row by row ja rahe hain
    row = [] # likha kyuki har baar nayi line banana hai
    for j in range(3): # inner loop (j) matlab column by column ja rahe hain
        row.append(matrix1[i][j] + matrix2[i][j]) # means dono matrix ke same jagah ke number jod rahe ho 
        # jaise (i = o ,j = 1) ho toh 2+8 = 10, (i = 1, j = 2) ho toh 6+4 = 10
        # fir row.append() mtlb result wale row mein ye answer chipka do 
    result.append(row) # ab jo row mein answer hai usko result wale box mein daal do
        # jab ek row complete ho jata hai toh result mein wo row add ho jata hai
for row in result:
    print(row)

print(f"\n{'='*30}")