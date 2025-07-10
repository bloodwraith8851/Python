print("Welcome to the Mystery Forest!")
print("You wake up in a tent in the middle of a dark jungle.")
print("your goal is to find your way back to civilization")

health = 100
has_map = False
found_compass = False
met_stranger = False

while True:
    print("\nPaths ahead:")
    print("1. Go north")
    print("2. Go South")
    choice = int(input("Choose a direction (1/2): "))

    if choice == 1:
        print("You walk into an thick fog and fall into hidden pit!")
        health -= 25
        print(f"Health: {health}")
        if health <= 0:
            print("You Succumbed to your injuries and died.")
            break
    elif choice == 2:
        print("You find a small abandoned shack")
        shack = input("Do you want to enter the shack? (yes/no): ").lower()
        if shack == "yes":
            print("Inside, You find a map and a compass.")
            has_map = True
            found_compass = True
        else:
            print("You walk past the shack.")

    if has_map and found_compass:
        print("\nYou use the map and compass to navigate safely.")
        stranger = input("Do you want to meet a stranger? (yes/no): ").lower()
        if stranger == "yes":
            print("They guide you to safety. You Win!")
            met_stranger = True
            break
        else:
            print("Your walk alone and fall into a trap. Game over.")
            break
    
    cont = input("Do you want to continue? (yes/no): ").lower()
    if cont != "yes":
        print("You camp in the forest. The end of the game.")
        break