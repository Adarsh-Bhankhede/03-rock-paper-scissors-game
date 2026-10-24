
#! Project Name: Rock-Paper-Scissors-Game

""""

Write a program to simulate a game of Rock, Paper, Scissors.
The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.

"""

print("\n=== Welcome To Rock Paper Scissors Game ===")

import random
choices = ('r', 'p', 's')
emojis = {'r':'🪨', 'p': '📃', 's': '✂️'}


while True:

    comp_choice = random.choice(choices)
    user_choice = input("\nChoose Rock, Paper or Scissor? (r/p/s): ").strip().lower()

    if user_choice not in choices:
        print("Invalid Choice!!!")
        continue
    
    print(f"you Choose {emojis[user_choice]}")
    print(f"Computer Choose {emojis[comp_choice]}")
    if user_choice==comp_choice:
        print("Tie..!")
    elif (
        (user_choice=='r' and comp_choice=='s') or
        (user_choice=='s' and comp_choice=='p') or
        (user_choice=='p' and comp_choice=='r')):

        print("You Win..!")
    else: 
        print("You Lose...!")
        
    play = input("Do you Want To Play Again? (y/n): ").strip().lower()
    if play == 'y':
        continue
    else:
        print("\n=== Thank You For Playing ===\n")
        break
