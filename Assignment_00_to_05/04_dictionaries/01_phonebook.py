'''
In this program we show an example of using dictionaries to keep track of information in a phonebook.
'''

def main():
    phonebook = {}
    
    while True:
        name = input("Name (Enter to stop): ")
        if not name:
            break
        phonebook[name] = input("Number: ")
    
    for name, number in phonebook.items():
        print(f"{name} -> {number}")
    
    while True:
        name = input("Lookup name (Enter to stop): ")
        if not name:
            break
        print(phonebook.get(name, "Not found"))

if __name__ == '__main__':
    main()
