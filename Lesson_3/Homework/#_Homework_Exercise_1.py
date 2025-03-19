# Homework Exercise 1

'''
Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.
'''


i: int = 1

# Massage showing that the program is running and how to end it
print("Program running, to end the programm digit 'end'\n")

# Start of the Cicle
while i > 0:
    
    # Word input 
    word: str = str(input("Put your word here: "))
    
    # Check if first character and last are identical
    if word[0] == word[-1]:
        print(f"Wow! The word, {word}, you have insert has the first and the last character identical!!")
        
    # If 'end' terminate the cicle
    elif word == "end":
        print("Program terminated!")
        break
        
    # If the word doesn't have the first and the last characters identical
    else:
        print(f"Sorry, this word, {word}, doesn't have the first and the last character identical, try again!")