'''
## Problem: High Low

We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

You make a guess, saying your number is either higher than or lower than the computer's number

If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

These steps make up one round of the game. The game is over after all rounds have been played.

'''

import random

NUM_ROUNDS = 5

def get_valid_guess():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ['higher', 'lower']:
        guess = input("Please enter either higher or lower: ").lower()
    return guess

def play_round(round_num, score):
    print(f"Round {round_num}")
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    print(f"Your number is {user_number}")
    
    guess = get_valid_guess()
    
    correct = False
    if guess == 'higher' and user_number > computer_number:
        correct = True
    elif guess == 'lower' and user_number < computer_number:
        correct = True

    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}\n")
    return score

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)
    
    print("Thanks for playing!")
    print()
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
