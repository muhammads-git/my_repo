# Guess the Number !game

import random

Aim = random.randint(1, 100)

while True:
    userChoice = input("Guess the number: ")
    userChoice = int(userChoice)
    
    if userChoice == Aim:
        print("Accomplished:")
        break
    elif userChoice < Aim:
        print("Too small GUESSING, Try Again")
    else:
        print("Too Big GUESSING, Try Again")

print(".....YOU WON! GUESSED SUCCESSFULLY.....")
