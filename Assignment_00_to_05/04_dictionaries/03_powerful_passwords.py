'''
You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

For example, using a hash function called SHA256(...) something as simple as

hello

can be hashed into a much more complex

2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)


'''

import hashlib

def hash_password(password):
    """Returns the SHA256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """Returns True if the given email's stored password hash matches the hash of password_to_check."""
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))  # False
    print(login("example@gmail.com", stored_logins, "password"))  # True
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # False
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # False
    print(login("student@stanford.edu", stored_logins, "password"))  # False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # True

if __name__ == '__main__':
    main()
