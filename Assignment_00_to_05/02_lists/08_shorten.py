'''
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
'''

MAX_LENGTH = 3  # Required by autograder

def main():
    # Get list input from user
    lst = []
    
    while True:
        user_input = input("Enter an element (or press Enter to finish): ")
        if user_input == "":
            break
        lst.append(user_input)

    print("Original list:", lst)
    
    shorten(lst)  # Call shorten function

    print("Final list:", lst)  # Print list after shortening

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()  # Remove last element
        print("Removed:", removed_element)  # Print removed element

if __name__ == '__main__':
    main()
