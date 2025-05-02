# Lesson 13 Exercise 9

'''
Esercizio 9.

Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.

'''
import re

def vowelRemover(txt:str):

    words: list = txt.split()

    if words == []:
        return ""
    else:
        new_word = re.sub(r"[aeiouAEIOU]", "", words[0])
        words.pop(0)
        txt = " ".join(words)
        return new_word + " " + vowelRemover(txt)
    
print(vowelRemover("Ciao sono Alessio e questa funzione levera tutte le vocali dalla frase in maniera recursiva"))
print(vowelRemover("Hello I'm Alessio and this function will remove all the vowels from the sentences in a recurseive way"))