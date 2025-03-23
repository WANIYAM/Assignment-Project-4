'''
Problem Statement
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2
'''

def main():
    # Get user input for the two numbers
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))

# Perform division and find the remainder
    quotient = num1 // num2
    remainder = num1 % num2

# Display the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()