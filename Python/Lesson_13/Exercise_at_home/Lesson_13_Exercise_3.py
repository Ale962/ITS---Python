# Lesson 13 Exercise 3

'''
Esercizio 3.

Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.

'''

def recursiveFactorial(n):

    if n == 1:
        return  1
    else:
        return n * recursiveFactorial(n-1)
    
print(recursiveFactorial(52))
print(recursiveFactorial(120))
print(recursiveFactorial(250))
print(recursiveFactorial(102))

