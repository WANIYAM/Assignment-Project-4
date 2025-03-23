'''
Problem Statement
Simulate rolling two dice, and prints results of each roll as well as the total.
'''
import random

def roll_die():
    """Roll a single die and return a random number between 1 and 6."""
    return random.randint(1, 6)

def main():
    # Roll two dice
    die1 = roll_die()
    die2 = roll_die()
    total = die1 + die2

    # Print results
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()
