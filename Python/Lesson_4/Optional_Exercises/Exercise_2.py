# Optional Exercise 2

'''
2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

'''

import random

def NumberGame() -> None:

    r_number = random.randint(0, 10)
    i = 5

    while i > 0:

        print(f"\nTry to guess the number, the number is within the range 0-10, you have {i} chances to guess it!")
        user_guess = int(input(f"write the number here: "))


        if i == 1 and user_guess != r_number:
            print("Sorry, you lost the game, better luck next time!")
            break

        if user_guess > r_number:
            print(f"You are too high! Lower your guess a bit!")
        
        if user_guess < r_number:
            print(f"You are too low! Aument your guess a bit!")

        if user_guess == r_number:
            print("Wow! Nice Guess, You won the game!")
            break

        i -= 1

if __name__ == "__main__":

    NumberGame()