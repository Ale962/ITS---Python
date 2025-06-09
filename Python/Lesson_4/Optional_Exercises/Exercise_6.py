# Optional Exercise 6

'''
6. Password Generator:

    Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.

'''

import random
import string

def generate_password() -> None: 
    print("--------------"*3)
    print()
    print('Password Generator Program')
    print()
    print("--------------"*3)
    print()
    lenght = int(input("Insert here the desired leght of the password: "))
    alfabetic_upper = int(input("Insert the number of uppercase letters characters desired: "))
    alfabetic_lower = int(input("Insert the number of lowercase letters characters desired: "))
    numeric = int(input("Insert the number of numeric characters desired: "))
    symbols = int(input("Insert the number of symbolic characters desired: "))
    print()
    print("--------------"*3)
    while True:
        if (alfabetic_upper + alfabetic_lower + numeric + symbols) > lenght:
            print()
            print("THE TOTAL OF THE CHARACTERS OF BOTH NUMERICAL AND ALFABETIC CHARACTERS ARE EXICIDING THE LENGHT DESIRED INSERTED!\nTRY DIFFERENT VALUE!")
            lenght = int(input("Insert here the desired leght of the password: "))
            alfabetic_upper = int(input("Insert the number of uppercase letters characters desired: "))
            alfabetic_lower = int(input("Insert the number of lowercase letters characters desired: "))
            numeric = int(input("Insert the number of numeric characters desired: "))
            symbols = int(input("Insert the number of symbolic characters desired: "))
            print()
            print("--------------"*3)
        elif (alfabetic_upper + alfabetic_lower + numeric + symbols) < lenght:
            print()
            print("THE TOTAL OF THE CHARACTERS OF BOTH NUMERICAL AND ALFABETIC CHARACTERS ARE LESS THEN THE LENGHT DESIRED INSERTED!\nTRY DIFFERENT VALUE!")
            lenght = int(input("Insert here the desired leght of the password: "))
            alfabetic_upper = int(input("Insert the number of uppercase letters characters desired: "))
            alfabetic_lower = int(input("Insert the number of lowercase letters characters desired: "))
            numeric = int(input("Insert the number of numeric characters desired: "))
            symbols = int(input("Insert the number of symbolic characters desired: "))
            print()
            print("--------------"*3)
        else:
            break
    password: str = ""
    l_up = 0
    l_lo = 0
    n = 0
    s = 0
    l_up_string = ""
    l_lo_string = ""
    num_string = ""
    symbols_string = ""
    while l_up < alfabetic_upper :
        l = random.choice(string.ascii_uppercase)
        l_up_string += l
        l_up += 1
    while l_lo < alfabetic_lower :
        l = random.choice(string.ascii_lowercase)
        l_lo_string += l
        l_lo += 1
    while n < numeric:
        num = random.choice(string.digits)
        num_string += num
        n += 1
    while s < symbols :
        sym = random.choice(string.punctuation)
        symbols_string += sym
        s += 1

    comb_string = l_lo_string + l_up_string + num_string + symbols_string
    chars = list(comb_string)
    random.shuffle(chars)
    password = "".join(chars)

    print()
    print('The Password is generated')
    print()
    print('PASSWORD: ' + password)
    print()
    print('Program terminated')

if __name__ == '__main__':
    generate_password()