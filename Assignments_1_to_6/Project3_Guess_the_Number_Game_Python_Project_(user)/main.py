# The user thinks of a number between a range (say 1–100), and the computer tries to guess it using feedback from the user (too high, too low, or correct).

import random

def computer_guesses_number():
    print("Think of a number between 1 and 100 and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one possible guess left

        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter H, L, or C.")

    print(f"🎉 Yay! I guessed it in {attempts} tries!")

# Run the game
computer_guesses_number()
