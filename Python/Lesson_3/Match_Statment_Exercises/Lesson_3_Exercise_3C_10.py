# Lesson 3 Exercise 3C-10

'''

Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.
Last modified: Friday, 28 February 2025, 2:50 PM

'''

day: str = input("Write the day here: ")
month: str = input("Write the month here: ")

match (day, month):

    case (1, 1):
        print(f"The day {day}/{month} is New Years's Day!")

    case (14, 2):
        print(f"The day {day}/{month} is S. Valentin!")

    case (2, 6):
        print(f"The day {day}/{month} is Italian Republic Day!")

    case (15, 8):
        print(f"The day {day}/{month} is Ferragosto!")

    case (31, 10):
        print(f"The day {day}/{month} is Halloween!")

    case (25, 12):
        print(f"The day {day}/{month} is Christmas!")

    case _:
        print(f"No important festivities or recurency in this date")

