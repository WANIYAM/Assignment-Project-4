'''
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
'''

def main():
    number_counts = {}
    
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if not user_input:
            break
        
        number = int(user_input)
        number_counts[number] = number_counts.get(number, 0) + 1
    
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
