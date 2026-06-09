""" Generate a random number 1–100. Let the user keep guessing until correct. 
Tell them 'higher' or 'lower' each time. Track number of guesses."""

import random

ran = random.randint(1,100)
print("Guess a number from 1 to 100 and win")
user_input = None
num_guess = 0
while user_input != ran:
    user_input = int(input("Enter number:"))
    num_guess += 1
    print(f"Guesses: {num_guess}")
    if user_input < ran:
        print(f"Hint: Higher")
    else:
        print(f"Hint: Lower")
else:
    print(f"You guessed it right. You won in {num_guess} guesses!! yeahwho...")