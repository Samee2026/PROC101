import random

while True:
    print("Rolling the dice...")
    dice = random.randint(1, 6)  # roll the dice
    print(f"You rolled a {dice}")

    response = input("Do you want to reroll? (y/n) ")
    if response.lower() == "n":
        break  # exit the loop