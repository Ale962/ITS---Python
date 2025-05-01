# Lesson 9 Exercise Lambda 5

'''
Esercizio 5 - Funzione lambda con if

Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".

'''

from typing import Callable

even_odd:Callable[[int],str]=lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_odd(5))
print(even_odd(12))
print(even_odd(7856191))
print(even_odd(5516816068410))