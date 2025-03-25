# Homework Exercise 8

'''
Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******
'''

# Settings Variables
i: int = 1
numbers: list = []

print("Program starting, write 5 integer numbers beetwen 1 and 30")

# Starting the loop to acquire the numbers
while i <= 5:
    
    n: int = int(input("Write the integer number here: "))  # Number input
    
    # If the number is in the target range it is stored and saved in the list
    if 1 <= n <= 30:
        numbers.append(n)
        i += 1
    
    # If the number is not in the target range it will not be stored and not counted as input
    else:
        print("Number not in the target range, please insert another number")
        
        
for number in numbers:
    print("*"*number)