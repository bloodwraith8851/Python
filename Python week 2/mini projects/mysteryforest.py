print("Welcome to the Mystery Forest!")  # Print the game title
print("You wake up in a tent in the middle of a dark jungle.")  # Print the game introduction
print("your goal is to find your way back to civilization")  # State the player's objective

health = 100  # Initialize player's health to 100
has_map = False  # Track if player has found the map
found_compass = False  # Track if player has found the compass
met_stranger = False  # Track if player has met the stranger

while True:  # Start the main game loop
    print("\nPaths ahead:")  # Show available paths
    print("1. Go north")  # Option to go north
    print("2. Go South")  # Option to go south
    choice = int(input("Choose a direction (1/2): "))  # Get player's direction choice

    if choice == 1:  # If player chooses north
        print("You walk into an thick fog and fall into hidden pit!")  # Describe event
        health -= 25  # Decrease health by 25
        print(f"Health: {health}")  # Show current health
        if health <= 0:  # If health is zero or less
            print("You Succumbed to your injuries and died.")  # Player dies
            break  # Exit the game loop
    elif choice == 2:  # If player chooses south
        print("You find a small abandoned shack")  # Describe finding a shack
        shack = input("Do you want to enter the shack? (yes/no): ").lower()  # Ask if player enters
        if shack == "yes":  # If player enters shack
            print("Inside, You find a map and a compass.")  # Describe finding items
            has_map = True  # Player now has map
            found_compass = True  # Player now has compass
        else:  # If player does not enter shack
            print("You walk past the shack.")  # Describe skipping shack

    if has_map and found_compass:  # If player has both map and compass
        print("\nYou use the map and compass to navigate safely.")  # Describe using items
        stranger = input("Do you want to meet a stranger? (yes/no): ").lower()  # Ask about meeting stranger
        if stranger == "yes":  # If player meets stranger
            print("They guide you to safety. You Win!")  # Player wins
            met_stranger = True  # Update status
            break  # Exit the game loop
        else:  # If player does not meet stranger
            print("Your walk alone and fall into a trap. Game over.")  # Player loses
            break  # Exit the game loop
    
    cont = input("Do you want to continue? (yes/no): ").lower()  # Ask if player wants to continue
    if cont != "yes":  # If player does not want to continue
        print("You camp in the forest. The end of the game.")  # End the game
        break  # Exit the