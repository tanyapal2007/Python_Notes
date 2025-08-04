import random

while True:
    print("Press Enter to roll the dice (or Ctrl + C to quit).....")
    dice = random.randint(1, 6)
    print(f"You Rolled a {dice}!")