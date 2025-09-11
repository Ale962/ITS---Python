# Lesson 9 Exercise Lambda 9

'''
Esercizio 9 - Ritorna una lambda

Scrivi una funzione moltiplicatore(n) che ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20

'''

from typing import Callable


multiplicatore: Callable[[int, int], int] = lambda x, y: x*y
per_due: Callable[[int], int] =lambda x: multiplicatore(x, 2)

if __name__ == '__main__':
    print(per_due(10))