from string import ascii_letters
import random
import re

lista1: list[int] = []

for x in range(20):
    if x % 2 == 0:
        n = x+1
        lista1.append(n)

lista2: list[int] = [x +1 for x in range(20) if x%2 == 0]

print(lista1)
print(lista2)

pool: list[str] = list(ascii_letters)

lista3: list[str] = [random.sample(pool, 20)]

print(lista3)

dict1: dict[int, int] = {x: x**3 for x in range(10) if x % 2 == 0}

print(dict1)

# Alternative Matrix Comprenhision

Matrix: list[list[int]] = [[x * y for x in range(1, 11)] for y in range(1, 11)]

for riga in Matrix:
    print(' '.join(str(x).rjust(5) for x in riga))


text = 'Hello, my Hello, name Hello'

hello = r'^Hello$'

hello_finded = re.findall(r'^Hello$', text)