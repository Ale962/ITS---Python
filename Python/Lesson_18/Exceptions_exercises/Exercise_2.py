# Lesson 18 Exercise 2

'''

Password Validation:  Write a function validate_password(password) that checks whether a password meets the following criteria: Minimum length of 20 characters, At least three uppercase letters, At least four special characters (non-alphanumeric). If the password is valid, the function should return True. If the password is invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria were not met.

'''

import re

class WrongCharactersPassword(Exception):
    """Password does not meet character requirements."""

def validate_password(password):
    errors = []

    if len(password) < 20:
        errors.append("Password must be at least 20 characters long.")

    if len(re.findall(r"[A-Z]", password)) < 3:
        errors.append("Password must contain at least 3 uppercase letters.")

    if len(re.findall(r"[^\w\s]", password)) < 4:
        errors.append("Password must contain at least 4 special characters.")

    if errors:
        raise WrongCharactersPassword("\n".join(errors))

    return "Password Valid"

    

try:
    print(validate_password("Ab!@CDEfghij12345678"))
except WrongCharactersPassword as e:
    print("Invalid Password:\n" + str(e))

try:
    print(validate_password("Ab!@CDEfghij12345678&$"))
except WrongCharactersPassword as e:
    print("Invalid Password:\n" + str(e))
