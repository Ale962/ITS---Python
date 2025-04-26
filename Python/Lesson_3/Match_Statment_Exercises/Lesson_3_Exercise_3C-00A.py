# Lesson 3 Exercise 3C-00A

'''Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

- Se il numero inserito è 1, stampare "Congratulazioni!"
- Se il numero inserito è 2, stampare "Wow! Gemelli!"
- Se il numero inserito è 3, stampare "Wow! Tre!"
- Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
- Se il numero inserito è 5, stampare "Incredibile! Cinque!"
- Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.

Expected Output:

Inserire il numero di neonati: 2
Wow! Gemelli!

- - - - - - - - - - - - - - - - - -

Inserire il numero di neonati: 5
Incredibile! Cinque!

- - - - - - - - - - - - - - - - - -

Inserire il numero di neonati: 7
Non ci credo! 7 bambini!'''

# Number of newborns
newborn: int = int(input("Put the number of the newborn here: "))

match newborn:
    
    # Number of newborn is 1
    case 1:
        print("Congratulations!!")

    # Number of newborns is 2
    case 2:
        print("Wow! Twins!")

    # Number of newborns is 3
    case 3:
        print("Wow! Three!")

    # Number of newborns is 4
    case 4:
        print("OMG!! Four Babies!!")

    # Number of newborns is 5
    case 5:
        print("Incredible!! Five!!")

    # Number of newborn is more then 5
    case _:
        print(f"I can't believe that! {newborn} babies!!")