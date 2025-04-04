'''
Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

'''


def main():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")
    
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

if __name__ == '__main__':
    main()
