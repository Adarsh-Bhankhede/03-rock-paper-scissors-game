# ✊ Rock-Paper-Scissors Game

**Week 3 - Project 3**

## 📌 Description

Write a Python program to simulate the classic **Rock-Paper-Scissors** game.

The player chooses Rock (`r`), Paper (`p`), or Scissors (`s`). The computer randomly selects its choice, and the program displays both choices using emojis and determines the winner according to the game rules.

The player can play multiple rounds until choosing to exit.

## 🎮 Game Rules

- 🪨 Rock beats Scissors.
- 📄 Paper beats Rock.
- ✂️ Scissors beats Paper.
- 🤝 If both choices are the same, the round is a tie.

## ✨ Features

- Allow the player to choose Rock, Paper, or Scissors.
- Generate a random choice for the computer.
- Display both choices using emojis.
- Determine the winner or a tie.
- Handle invalid user input.
- Allow the player to play again.

## 🔄 Program Flow

1. Display the welcome message.
2. Randomly select the computer's choice.
3. Ask the player to enter `r`, `p`, or `s`.
4. Validate the player's input.
5. Display the player's and computer's choices.
6. Determine and display the result.
7. Ask the player whether they want to play again.
8. If the player enters `y`, start another round; otherwise, exit the game.

## 🛠️ Concepts Used

- `random` module
- `random.choice()`
- `while` loop
- `if-elif-else` statements
- Tuples
- Dictionaries
- User input and string methods
- Conditional logic
- F-strings
