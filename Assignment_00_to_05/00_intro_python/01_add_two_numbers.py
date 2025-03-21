'''
## Problem Statement

Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

1. Prompt the user to enter the first number.

2. Read the input and convert it to an integer.

3. Prompt the user to enter the second number.

4. Read the input and convert it to an integer.

5. Calculate the sum of the two numbers.

6. Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

'''



def main():
    # Prompt the user to enter the first number
    num1 = input("Enter the first number: ")
    # Read the input and convert it to an integer.
    num1 = int(num1)
    # Prompt the user to enter the second number
    num2 = input("Enter the second number: ")
    # Read the input and convert it to an integer.
    num2 = int(num2)

    # Calculate the sum of the two numbers.
    total = num1 + num2
    print(f"Type of sum: {type(total)}")

    # Print the total sum with an appropriate message.
    print(f"The sum of {num1} and {num2} is {total}")

# Call the main function
if __name__ == "__main__":
    main()