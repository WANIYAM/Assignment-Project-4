'''
Write a function that takes a list of numbers and returns the sum of those numbers.
'''
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    result = sum_numbers(numbers)
    print(result)

if __name__ == '__main__':
    main()
