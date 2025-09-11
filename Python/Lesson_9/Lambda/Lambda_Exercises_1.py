# Lesson 9 Exercise Lambda 1

'''
Esercizio 1 - Sintassi

Scrivi una funzione lambda che prenda un numero intero e ritorni il suo quadrato.

Esempio atteso:

quadrato = lambda x: ...

'''

from typing import Callable

square: Callable[[int], int] =  lambda x: x**2

if __name__ == '__main__':
    print(square(5))
    print(square(10))