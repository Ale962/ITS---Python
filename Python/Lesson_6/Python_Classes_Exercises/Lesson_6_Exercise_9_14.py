# Lesson 6 Exercise 9.14

'''
9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

'''

import random
import string

class LotteryMachine:

    def __init__(self):
        self.__winner = []
        self.draw_winner()
        

    def draw_winner(self):
        pool: list = list(range(10)) + list(string.ascii_letters)
        self.__winner = random.sample(pool, 4)

    def get_winner(self):
        return self.__winner
    
    def __str__(self):
        winning_string = " ".join(str(x) for x in self.__winner)
        return f"And Finally the winnig ticket is: {winning_string}"

ticket1 = LotteryMachine()
ticket2 = LotteryMachine()

print(ticket1)
print(ticket2)