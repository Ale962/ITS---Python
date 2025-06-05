# Optional Exercise 6

'''
6. Password Generator:

    Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.

'''

import random
import string

def generate_password() -> str: 
    lenght = int(input("Insert here the desired leght of the password: "))
    alfabetic = int(input("Insert the number of alfabetical characters desired: "))
    numeric = int(input("Insert the number of numeric characters desired: "))
    while True:
        if (alfabetic + numeric) > lenght:
            print("The total characters both numerical and alfabetic are exciding the lenght inserted insert different value")
            lenght = int(input("Insert here the desired leght of the password: "))
            alfabetic = int(input("Insert the number of alfabetical characters desired: "))
            numeric = int(input("Insert the number of numeric characters desired: "))
        elif (alfabetic + numeric) < lenght:
            print("The total characters both numerical and alfabetic are less of the lenght inserted, reinsert different values")
            lenght = int(input("Insert here the desired leght of the password: "))
            alfabetic = int(input("Insert the number of alfabetical characters desired: "))
            numeric = int(input("Insert the number of numeric characters desired: "))
        else:
            break
    password: str = ""
    a = 0
    n = 0
    alf_string = ""
    num_string = ""
    while a < alfabetic:
        l = random.choice(string.ascii_letters)
        alf_string += l
        a += 1
    while n < numeric:
        num = random.randrange(0,10)
        num_string += str(num)
        n += 1

    comb_string = alf_string + num_string
    chars = list(comb_string)
    random.shuffle(chars)
    password = "".join(chars)

    return password