# Lesson 9 Exercise Lambda 2

'''
Esercizio 2 - Somma di due numeri

Crea una funzione lambda che accetti due numeri e restituisca la loro somma.

'''

from typing import Callable

summ: Callable[[int, int], int] = lambda x, y: x + y

print(summ(4, 5))
print(summ(3254, 55211))
print(summ(5198641831, 98354))