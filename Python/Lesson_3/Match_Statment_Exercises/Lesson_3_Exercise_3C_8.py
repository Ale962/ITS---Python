# Lesson 3 Exercise 3C-8

'''
Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:

frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"

- - - - - - - - - - - - - - - - - - - - - -

frase: ho vinto!
Output: Wow!

'''

while True:

    statement: str = input("Write here your statement: ")

    match statement:

        case s if s[-1] == "?" and len(s) % 2 == 0:
            print("Yes\n")

        case s if s[-1] == "?" and len(s) % 2 != 0:
            print("No\n")

        case s if s.endswith("!"):
            print("Wow!\n")

        case _:
            print(f"You are saying {statement}\n")

    add_stat: str = input("Want to add a new statment? (Y or N): ")

    if add_stat.upper() == "N":
        break