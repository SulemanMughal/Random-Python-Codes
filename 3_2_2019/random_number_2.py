import random

pets = ["Dog", "Fish", "Cat", "Lizard", "Hamster", "Gerbil", "Birds", "Equine" ]
print("Your pets:")
for item in pets:
    choice = random.choice(pets)
    pets.remove(choice)
    print(choice)
