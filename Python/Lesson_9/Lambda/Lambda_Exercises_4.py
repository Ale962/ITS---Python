# Lesson 9 Exercise Lambda 4

'''
Esercizio 4 - Ordinamento con sorted()

Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]. Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.

'''

students: list = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

by_age_studs: list = list(sorted(students, key = lambda student: student[1]))

print(by_age_studs)