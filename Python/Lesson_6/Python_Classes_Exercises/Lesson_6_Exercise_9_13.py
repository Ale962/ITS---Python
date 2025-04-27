# Lesson 6 Exercise 9.13

'''
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

'''

import random

class Die:

    def __init__(self, sides: int = 6):
        self.set_sides(sides)

    def set_sides(self, sides) -> None:
        self.__sides = sides

    def get_sides(self) -> int:
        return self.__sides
    
    def roll_die(self) -> int:
        face = random.randint(1, self.__sides)
        return face
    
def times_to_rolls(x: int, die: Die) -> None:
    results: list = [str(die.roll_die()) for _ in range(x)]
    print(" ".join(results))



die1 = Die()
die2 = Die(10)
die3 = Die(20)

times_to_rolls(10, die1)
print("\n")
times_to_rolls(10, die2)
print("\n")
times_to_rolls(10, die3)