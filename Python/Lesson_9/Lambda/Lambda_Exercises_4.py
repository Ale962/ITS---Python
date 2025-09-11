# Lesson 9 Exercise Lambda 4

'''
Esercizio 4 - Ordinamento con sorted()

Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]. Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.

'''

students: list[tuple[str, int]] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

by_age_studs: list[tuple[str, int]] = list(sorted(students, key = lambda student: student[1]))

# Alternative sorting method
students.sort(key=lambda s: s[1])

if __name__ == '__main__':
    print(by_age_studs)
    print(students)