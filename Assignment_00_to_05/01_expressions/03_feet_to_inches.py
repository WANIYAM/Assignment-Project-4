'''
Problem Statement
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
'''

def main():
    # Ask the user for the number of feet
    feet = float(input("Enter the number of feet: "))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12

    # Display the result
    print(f"{feet} feet is equal to {inches:.2f} inches.")

# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
