# Lesson 3 Exercise 3C-2

'''
Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0

- - - - - - - - - - - - - - - - -

Inserisci il voto di laurea: 65
Output: Voto non valido

'''

vote: int = int(input("Insert the vote here, please only an integer number between 66 and 110: "))

match vote:
    case range(106, 111):
        print("GPA: 4.0")

    case range(101, 106):
        print("GPA: 3.7")

    case range(96, 101):
        print("GPA: 3.3")

    case range(91, 96):
        print("GPA: 3.0")

    case range(86, 91):
        print("GPA: 2.7")

    case range(81, 86):
        print("GPA: 2.3")

    case range(76, 81):
        print("GPA: 2.0")

    case range(70, 76):
        print("GPA: 1.7")

    case range(66, 70):
        print("GPA: 1.0")

    case _:
        print("Vote inserted not valid. Either a string, a float or an integer number outside the given range inserted.")