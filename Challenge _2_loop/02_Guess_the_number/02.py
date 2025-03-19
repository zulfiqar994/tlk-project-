

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
# User guessing loop
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret_number:
        print("Correct! 🎉")
        break
    else:
        print("Wrong, try again!")

