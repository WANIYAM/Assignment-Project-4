'''
The program asks:

How many passwords do you want to generate?

How long should each password be?

Then it outputs secure random passwords with letters, numbers, and symbols.
'''

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("How long should each password be? "))

        print("\nHere are your passwords:")
        for _ in range(num_passwords):
            print(generate_password(length))
    except ValueError:
        print("⚠️ Please enter valid numbers!")

main()
