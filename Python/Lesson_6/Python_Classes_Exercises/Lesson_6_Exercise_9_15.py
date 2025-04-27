'''
9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.

2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

    Your ticket
    The winning ticket
    How many attempts it took to win

Last modified: Monday, 31 March 2025, 10:52 AM

'''

import random
import string

class LotteryMachine:

    def __init__(self):
        self.__winner = ""
        self.draw_winner()
        
        

    def draw_winner(self) -> list:
        pool: list = list(range(10)) + list(string.ascii_letters)
        winner = random.sample(pool, 4)
        self.__winner = " ".join(str(x) for x in winner)
        return self.__winner
    
    def draw_ticket(self) -> list:
        pool: list = list(range(10)) + list(string.ascii_letters)
        draw_ticket_list = random.sample(pool, 4)
        draw_ticket = " ".join(str(x) for x in draw_ticket_list)
        return draw_ticket

    def get_winner(self) -> list:
        return self.__winner
    
    def __str__(self) -> str:
        return f"And Finally the winnig ticket is: {self.__winner}"

    def simulate_until_win(self, my_ticket: list) -> str:

        i = 1

        my_tick_str = " ".join(str(y) for y in my_ticket)

        while True:

            drawn_ticket = self.draw_ticket()

            if my_tick_str == drawn_ticket:
                break
            else:
                i += 1


        return f"Your Ticket is {my_tick_str}\nThe winning ticket is{drawn_ticket}\nTo win it needed {i} iteration"





'''
    def simulate_until_win(self, my_ticket) -> str:
        
        self.__winner = self.draw_winner()
        my_ticket = self.draw_winner()

        winner = " ".join(str(x) for x in self.__winner)
        ticket = " ".join(str(y) for y in my_ticket)

        i = 1

        while my_ticket != self.__winner:

            my_ticket = self.draw_winner()
            i += 1


        return f"Your ticket is {ticket}\nThe winning ticket is {winner}\nIt tooks {i} attempts to win"

'''

ticket1 = LotteryMachine()

my_ticket = ["9" "c" "2" "A"]

result = ticket1.simulate_until_win(my_ticket)
print(result)