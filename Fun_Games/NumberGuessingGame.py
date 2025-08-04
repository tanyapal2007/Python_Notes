import random

number = random.randint(1 , 100)
attempts = 0
print("Guess the number betwwen 1 to 100")

while True:
    guess = int(input("Enter your Guess"))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"The number was {number}. You Guessed it in {attempts} attempts.")
        break
