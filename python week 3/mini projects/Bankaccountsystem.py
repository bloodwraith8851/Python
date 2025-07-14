import random
accounts = {}

def generate_account_number():
    num = random.randint(100000000000, 999999999999) # Generate a random 12-digit number 
    return f"{str(num)[:4]}-{str(num)[4:8]}-{str(num)[8:]}" # Return the first 4 digits, the next 4 digits, and the last 4 digits 1234 1234 1234
def create_account():
    print ("\n ----Create an account---- \n")
    name = input("Enter your name: ")
    adress = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    try:
        balance = float(input("Enter your initial balance: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    acc_num = generate_account_number()
    accounts[acc_num] = {
        "name": name,
        "address": adress,
        "phone": phone,
        "balance": balance
    }
    print("Account created successfully!")
    print(f"Account number: {acc_num}")
    print(f"Name: {name}")
    print(f"Address: {adress}")
    print(f"Phone number: {phone}")
    print(f"Balance: {balance}")

def deposit():
    print ("\n ----Deposit---- \n")
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        try:
            amount = float(input("Enter the amount to deposit: "))
            accounts[acc_num]["balance"] += amount
            """
            step 1
            balance = accounts[acc_num]["balance"]
            step 2
            balance += amount
            step 3
            accounts[acc_num]["balance"] = balance
            """
            print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{accounts[acc_num]['balance']:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Account not found.")

def withdraw():
    print ("\n ----Withdraw---- \n")
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= accounts[acc_num]["balance"]:
                accounts[acc_num]["balance"] -= amount
                print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{accounts[acc_num]['balance']:.2f}")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Account not found.")

def checkbalance():
    print ("\n ----Check Balance---- \n")
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        print(f"Account number: {acc_num}")
        print(f"Name: {accounts[acc_num]['name']}")
        print(f"Balance: Rs.{accounts[acc_num]['balance']:.2f}")
    else:
        print("Account not found.")

def accdetails():
    print ("\n ----Account Details---- \n")
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        print(f"Account number: {acc_num}")
        print(f"Name: {accounts[acc_num]['name']}")
        print(f"Address: {accounts[acc_num]['address']}")
        print(f"Phone number: {accounts[acc_num]['phone']}")
        print(f"Balance: Rs.{accounts[acc_num]['balance']:.2f}")
    else:
        print("Account not found.")

def deleteaccount():
    print ("\n ----Delete Account---- \n")
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        del accounts[acc_num]
        print("Account deleted successfully!")
    else:
        print("Account not found.")


while True:
    print("\n ----Bank Account System---- \n")
    print("1. Create an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Account details")
    print("6. Delete account")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        checkbalance()
    elif choice == "5":
        accdetails()
    elif choice == "6":
        deleteaccount()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

       