# Lesson 9 Exercise Lambda 7

'''
Esercizio 7 - Filtra parole corte

Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"] Estrai solo le parole con più di 4 lettere usando filter() e lambda.

'''
import re

parole = ["cane", "gatto", "elefante", "ratto", "orso"]

f_letters = list(filter(lambda x: re.fullmatch(r"[A-Za-z]{4}", x), parole))

print(f_letters)