# # multiplication (1 to 10)

for i in range(1,11): 
    for j in range(1,11):
        print (f"{i} x {j} = {i*j}")
    print()

# # diamond shape

n = 5 # height of the diamond (number of rows in the upper half)

# upper half

for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))

# lower half

for i in range(n-1,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))

# # n-i-1 = 5-0-1 = 4
# # 2*i+1 = 2*0+1 = 1


# # numeric pyramid

r = 5 # rows
for o in range(1,r+1): # outer loop
    print(" "*(r-o),end="") # spaces
    
    for j in range(1,o+1): # inner loop
        print(j,end=" ") # print numbers
    print() # new line

#pending

# rows = 5
# for i in range(1, rows+1):
#   print(" "*(rows-i) + " ".join(str(j) for j in range(1, i+1)))

# CLI pattern Designer Tool

def print_star_pyramid(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))

def print_number_triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def main():
    while True:
        print("\n --- Pattern Designer --- \n")
        print("1. Star Pyramid")
        print("2. Numeric Triangle")
        print("3. Exit")
        choice = input("Enter Your Choice:")

        if choice == "1":
            size = int(input("Enter the size of the pyramid: "))
            print_star_pyramid(size)
        elif choice == "2":
            size = int(input("Enter the size of the triangle: "))
            print_number_triangle(size)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()