# The computer randomly selects a word, and the user has to guess it letter by letter before running out of tries.

import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'code', 'tutorial']
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    lives = 6

    print("🎮 Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))

        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_display))

        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
            elif guess in word_letters:
                guessed_letters.add(guess)
                word_letters.remove(guess)
                print("✅ Good guess!")
            else:
                guessed_letters.add(guess)
                lives -= 1
                print("❌ Wrong guess.")
        else:
            print("⚠️ Invalid input. Please enter a single letter.")

    if lives == 0:
        print("\n💀 You lost. The word was:", word)
    else:
        print("\n🎉 You guessed the word:", word)

# This line starts the game:
hangman()
