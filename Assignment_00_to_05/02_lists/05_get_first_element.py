'''
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
'''

def main():
    lst = []
    
    while True:
        user_input = input("Enter an element (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        
        # Convert input to int if possible, otherwise keep as string
        try:
            lst.append(int(user_input))
        except ValueError:
            lst.append(user_input)

    print("You've finished entering elements. The first element is:", get_first_element(lst))
    return lst

def get_first_element(lst):
    """Returns the first element of a non-empty list."""
    return lst[0]

if __name__ == '__main__':
    main()
