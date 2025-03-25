# Homework Exercise 2

'''
Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.
'''

# Definition of the variable and the counter
string: str = str(input("Write your phrase here: "))
i: int = 0

# Cicle to count spaces in the string
for characters in string:
    
    if characters == " ":
        i += 1

# Print of the result
print(f"The number of spaces in the string is: {i}")