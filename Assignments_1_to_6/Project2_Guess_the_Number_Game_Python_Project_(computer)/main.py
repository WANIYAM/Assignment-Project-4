import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100...")

    # Computer chooses a number
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number!")

# Start the game
guess_the_number()
