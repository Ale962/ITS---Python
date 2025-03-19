# Homework Exercise 3

'''
Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.
'''

# Input of the string to be converted and start of the program 
string: str = str(input("Write your phrase or word here: "))

# Inverted string variable to be saved
string_inverted: str = ""

# Cicle to ivert the string
while True:
    string_inverted = string[::-1]
    break

# Print of the inverted phrase or word
print(f"The string inverted is: {string_inverted}")