# Lesson 9 Exercise Lambda 8

'''
Esercizio 8 - Doppio ordinamento

Hai una lista di dizionari:

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

Ordina la lista in ordine decrescente di media usando una funzione lambda.

'''

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

average_order: list = list(sorted(studenti, key = lambda student: student["media"] ))

print(average_order)