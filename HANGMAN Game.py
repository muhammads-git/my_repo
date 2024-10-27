# Hangman game .....
import random
print("..........WELCOME TO HANGMAN ...........")
#list of subjects !
list = ["Pyhsics","Bio","Chemistry","English","Math"]
pc_choses = random.choice(list)

attempt = 5
score = 0
winning_score = 5

print("You cannot defeat Me!\nI am smarter than You")
while True:
    print(list)
    user_choice = input("Guess the subject: ")
    if user_choice == pc_choses:
        print(f"You choses {user_choice} and computer choses {pc_choses}:")
        print("You win")
        score += 1
        print("You current score is ",score)
    else:
        print(f"You choses {user_choice} and computer choses {pc_choses}:")
        print("Wrong , try again ")
        attempt -= 1
        print("Attempt left",attempt)
    if attempt == 3:
        print("Computer is so smart! Haha")
        print("But I'll not give up! budddy")
    if attempt == 0:
        print("0 attempt left, Game Ends:")
        break
    if score == 3:
        print("Hey! Computer I am gonna smash you !")
    if score == winning_score:
        print("You won the Game: CONGRATULATIONs!")
        