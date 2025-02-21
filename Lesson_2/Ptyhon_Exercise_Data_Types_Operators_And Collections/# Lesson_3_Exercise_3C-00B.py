# Lesson 3 Exercise 3C-00B

'''
Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente di inserire il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.

Expected Output:

Inserire nome: Luca
Inserire gender. Digitare m per maschio e f per femmina: m
Nome: Luca
Gender: Maschio

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Inserire nome: Anna
Inserire gender. Digitare m per maschio e f per femmina: f
Nome: Anna
Gender: Femmina

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Inserire nome: Alex
Inserire gender. Digitare m per maschio e f per femmina: x
Mi dispiace Alex, non e' possibile procedere con la generazione di un documento di identità!
'''

# Name and Gender
name: str = str(input("Put your name here: "))
gender: str = str(input("What is your gender? m/f: "))

match (name, gender):
    
    # If is Male
    case (name, m):
        print(f"Name: {name}, Gender: MALE")

    # If is Female
    case (name, f):
        print(f"Name: {name}, Gender: FEMALE")

    # If the Gender is not recognised
    case _:
        print("Error it is not possible to create an identity card")