# Lesson 9 Exercise Lambda 6

'''
Esercizio 6 - Uso con reduce()

Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].

'''
from functools import reduce

numbers: list = [2, 3, 4]

product: int = reduce(lambda x, y: x * y, numbers)

print(product)