# Lesson 9 Exercise Lambda 9

'''
Esercizio 9 - Ritorna una lambda

Scrivi una funzione moltiplicatore(n) che ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20

'''

from typing import Callable


def product(n: int) -> Callable[[int], int]:

    return lambda x: x * n

per = product(5)

print(per(10))