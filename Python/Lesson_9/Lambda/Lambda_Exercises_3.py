# Lesson 9 Exercise Lambda 3

'''
Esercizio 3 - Uso con filter()

Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. Usa filter() con una lambda per ottenere solo i numeri pari.

'''

numbers: list[int] = [5, 12, 17, 18, 24, 32]
evens: list[int] = list(filter(lambda a: a % 2 == 0, numbers))

if __name__ == '__main__':
    print(evens)