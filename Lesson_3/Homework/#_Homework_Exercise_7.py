# Homework Exercise 7

'''
Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.
'''
# List a and b
a: list = list(range(0, 101, 10))
b: list = list(range(0, 31, 3))

# I didn't know how to do this, I searched on the internet for a solution and encounter the zip() function, I don't know if we are supposed to do so for this Homework
# here is the link in which I found this function https://stackoverflow.com/questions/44829897/add-values-from-lists-of-same-length-in-python
c: list = [x+y for x, y in zip(a, b[::-1])]


print(f"{a}, {b}, {c}")