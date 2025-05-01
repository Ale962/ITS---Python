# Lesson 3 Exercise 6C-7

'''
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%

'''

i: int = 0
tcount: int = 0
ccount: int = 0

print("Insert the result of the launch here: (T or C)")

while i < 8:

    result: str = input()

    match result.upper():
    
        case "T":
            tcount += 1
            i += 1
            print(f"Launch {i}: {result}")
        
        case "C":
            ccount += 1
            i += 1
            print(f"Launch {i}: {result}")

        case _:
            print("Result not recognised, launch the coin again!")



c_percent: float = (ccount/i)*100
t_percent: float = (tcount/i)*100

print(f"\nTotal 'Head': {tcount}")
print(f"Percentul 'Head': {t_percent}")

print(f"\nTotal 'Cross': {ccount}")
print(f"Percentul 'Cross': {c_percent}")