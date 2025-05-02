# Lesson 13 Exercise 10

'''

Esercizio 10.

Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".


'''
import re

def charDuplicator(text: str):

    words: list = text.split()

    if not words:
        return ""
    else:
        word = re.sub(r"([A-Za-z])", r"\1\1",words[0])
        words.pop(0)
        text: str = " ".join(words)
        return word + " " + charDuplicator(text)
    
print(charDuplicator("Questa funzione duplicherà tutti i caratteri della frase"))
print(charDuplicator("This function will duplicate each character of this phrase"))