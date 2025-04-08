# The user and computer each choose rock, paper, or scissors. The program compares them and decides who wins.

import random

def play():
    user = input("Choose Rock, Paper, or Scissors: ").lower()
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win! 🎉"
    elif user in choices:
        return "You lose. 😢"
    else:
        return "Invalid choice. Try again!"

# Game loop
while True:
    print(play())
    again = input("Play again? (yes/no): ").lower()
    if again != 'yes':
        break
