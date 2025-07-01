# Resturant billing system using nested if statement
print ("Welcome to our Resturant")
print ("menu:")
print ("1. Pizza\n2. Burger\n3. Pasta\n")

item_detail = ""
choice = input("choose an item from the menu:").lower()
if choice == "pizza":
    print("pizza sizes:\n1. Small - ₹150\n2. Medium - ₹250\n3. Large - ₹350\n")
    size = input("choose a size:").lower()
    item_detail = f"Pizza, {size.capitalize()}"
    if size == "small":
        price = 150
        print("your total bill is: ₹150")
    elif size == "medium":
        price = 250
        print("your total bill is: ₹250")
    elif size == "large":
        price = 350
        print("your total bill is: ₹350")
    else:
        price = 0
        print("invalid size")
elif choice == "burger":
    print("burger types:\n1. Veg - ₹100\n2. Non-veg - ₹150\n")
    type = input("choose a type:").lower()
    item_detail = f"Burger, {type.capitalize()}"
    if type == "veg":
        price = 100
        print("your total bill is: ₹100")
    elif type == "non-veg":
        price = 150
        print("your total bill is: ₹150")
    else:
        price = 0
        print("invalid type")
elif choice == "pasta":
    print("pasta flavors:\n1. Tomato - ₹100\n2. Cheese - ₹150\n")
    flavor = input("choose a flavor:").lower()
    item_detail = f"Pasta, {flavor.capitalize()}"
    if flavor == "tomato":
        price = 100
        print("your total bill is: ₹100")
    elif flavor == "cheese":
        price = 150
        print("your total bill is: ₹150")
    else:
        price = 0
        print("invalid flavor")
else:
    print("invalid choice")
    price = 0

if price > 0:
    try:
        quantity = int(input("Enter quantity:"))
        total = price * quantity
        print("\nAre you a registered customer? (yes/no)")
        registered = input().lower()
        if registered == "yes":
            print("\n1. Regular\n2. VIP")
            role = input("Choose a role:").lower()
            if role == "regular":
                discount = 0.1
            elif role == "vip":
                discount = 0.2
            else:
                discount = 0
        else:
            discount = 0
        final_amount = total - (total * discount)
        print ("/n Choose payment method:")
        print ("\n1. Cash\n2. Card")
        payment = input("choose a payment method:").lower()
        if payment == "cash":
            print ("please pay at the counter")
        elif payment == "card":
            print ("processing card payment...")
            print ("payment successful")
        else:
            print ("invalid payment method")
        print (f"\n --- Order Summary --- \n")
        print(f"Item: {item_detail}")
        print (f"price per unit: ₹{price}")
        print (f"Quantity: {quantity}")
        print (f"subtotal: ₹{total}")
        print (f"Discount: ₹{discount * total}")
        print (f"Final Amount: ₹{final_amount:.2f}")
        print ("\n --- Thank You ---")
    except ValueError:
        print ("invalid quantity input please try again :) :) :)")
    