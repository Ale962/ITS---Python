# Lesson 3 Exercise 3C-1

'''
Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto: 5
Output: Insufficiente
- - - - - - - - - - -
Inserisci il voto: 11
Output: Voto non valido

'''

vote: int = int(input(f"Write the student vote here, please insert only integer number with value between 1 and 10: "))

match vote:
    
    case range(1, 4):
        print("Badly insufficient")

    case range(4, 6):
        print("Insufficient")

    case range(6, 8):
        print("Sufficient")

    case range(8, 10):
        print("Very Good")

    case 10:
        print("Excellent")

    case _:
        print("Vote inserted not valid. Either a string, a float or an integer number outside the given range inserted.")