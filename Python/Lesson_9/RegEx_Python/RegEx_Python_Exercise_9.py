# Lesson 9 Exercise RegEx in Python 9

'''
9. Trova tutti i codici fiscali in un testo

Scrivi una funzione find_fc(text) che trova tutti i codici fiscali all'interno di un testo.

Esempio:

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']

'''

import re

def find_fc(text):
    return re.findall(r"[A-Z0-9]{16}", text)

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."

print(find_fc(testo))