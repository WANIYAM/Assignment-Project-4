'''
Problem Statement
Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
'''

import random
def main():
    # Initialize variables
    die1 = 0
    die2 = 0
    # Roll the dice three times
    for i in range(3):
        # Roll the first die
        die1 = random.randint(1, 6)
        # Roll the second die
        die2 = random.randint(1, 6)
        # Print the results of each die roll
        print(f"Die 1: {die1}, Die 2: {die2}")
if __name__ == '__main__':
    main()