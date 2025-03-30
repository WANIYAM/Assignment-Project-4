'''
There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

Here is an example run of the program (user input is in bold italics):

How many (apple) do you want?: 2

How many (durian) do you want?: 0

How many (jackfruit) do you want?: 1

How many (kiwi) do you want?: 0

How many (rambutan) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5
'''
def main():
    # Dictionary of fruits with their respective prices
    fruit_prices = {
        "apple": 3.0,
        "durian": 15.0,
        "jackfruit": 10.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.5
    }
    
    total_cost = 0
    
    # Loop through each fruit and ask the user how many they want
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price
    
    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")

# Required to call the main function
if __name__ == '__main__':
    main()

