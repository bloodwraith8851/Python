# shopping list manager

# create an empty list to store the shopping list
shopping_list = []

# function to add an item to the shopping list
while True:
    action = input("Add/Remove/View/Exit: ").lower()
    if action == "add":
        iteam = input("Enter the iteam: ")
        shopping_list.append(iteam) # add iteam to the list
        print("Iteam added to the list.")
        if iteam in shopping_list:
            print("Iteam already in the list.")
        elif iteam not in shopping_list:
            print("Iteam added to the list.")
    elif action == "remove":
        iteam = input("Enter the iteam: ")
        if iteam in shopping_list:
            shopping_list.remove(iteam) # remove iteam from the list
            print("Iteam removed from the list.")
        else:
            print("Iteam not found in the list.")
    elif action == "view":
        print("Shopping List:", shopping_list) # print the shopping list
    elif action == "exit":
        print("Goodbye!")
        break # exit the loop
    else:
        print("Invalid action. Please try again.")

    