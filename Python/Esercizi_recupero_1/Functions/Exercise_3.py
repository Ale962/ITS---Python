# Exercise 3

'''
Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}

'''
import string

def WordsCounter(text: str) -> dict[str, int]:
    puntaction: str = string.punctuation
    list_words: list[str] = text.split()
    words_counter: dict[str, int] = {}

    for word in list_words:
        w = word.lower().strip(puntaction)
        if w not in words_counter:
            words_counter[w] = 1
        elif not w:
            continue
        else:
            words_counter[w] += 1
    
    return words_counter


if __name__ == '__main__':
    text1 = "Hello, world! Hello... PYTHON? world."
    text2 = "Cats, dogs; birds. CATS!! Dogs? cats."
    text3 = "...,,,!!!???"
    text4 = ""
    text5 = "Test, test. TEST! test??"
    text6 = "L’uomo, stanco e affamato, urlò: 'Pane! Vino!'"

    print(WordsCounter(text1))
    print(WordsCounter(text2))
    print(WordsCounter(text3))
    print(WordsCounter(text4))
    print(WordsCounter(text5))
    print(WordsCounter(text6))