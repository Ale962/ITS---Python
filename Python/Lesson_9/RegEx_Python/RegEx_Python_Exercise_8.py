# Lesson 9 Exercise RegEx in Python 8

'''
8. Trova parole con lettere maiuscole e numeri

Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e/o numeri.

Esempio:

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678', 'XYZZYZZZ']

'''

import re

def find_codes(text: str):
    return re.findall(r"[A-Z0-9]{8}", text)

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"

print(find_codes(text))