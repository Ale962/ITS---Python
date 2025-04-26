# Lesson 10 Exercise 5

'''
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!

Expected output:

print(integerPower(3, 4)) --> 81

print(integerPower(2, 5)) --> 32

'''

def integerPower(b: int, e: int) -> int:

    result = 1

    if (e%1 == 0) and (e > 0) and (b%1 == 0):

        for i in range(e):
            result *= b

    return result

print(integerPower(3, 4))
print(integerPower(2, 5))
print(integerPower(8, 10))
print(integerPower(18, 4))