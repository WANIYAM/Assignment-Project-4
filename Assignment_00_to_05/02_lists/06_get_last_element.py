'''
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
'''

def main():
    lst = []
    
    while True:
        user_input = input("Enter an element (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        lst.append(user_input)
    
    print("You've finished entering elements. The last element is:", get_last_element(lst))

def get_last_element(lst):
    """Returns the last element of a non-empty list."""
    return lst[-1]  # Using negative index to get the last element

if __name__ == '__main__':
    main()
