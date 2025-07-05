import random

secret = random.randint(1,20)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Enter a number between 1 and 20: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    tries += 1

print(f"You guessed the number in {tries} tries!" )