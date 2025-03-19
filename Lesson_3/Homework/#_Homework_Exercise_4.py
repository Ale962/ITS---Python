# Homework Exercise 4

'''
Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).
'''

# Variables needed
i: int = 1                          # counter
sum_int: int = 0                    # sum of integer numbers
average_int: float = 0                # average of all numbers
max_n: float = float("-inf")        # max number
min_n: float = float("inf")         # min number

print("Program running, to end the program write a negative number")

n: float = float(input("Write your number here: "))

# Keep the program running until a negative number is inserted as input
while n >= 0:
    
    # Check for max and min
    if n > max_n:
        max_n = n
    if n < min_n:
        min_n = n
    
    # Check if it is an integer number to be added to the sum of integers     
    if n.is_integer():
        sum_int += int(n)       # Searched on the internet, it was adding the float numbers to this sum with n only, the int(n) prevented that
        # Calculation of the average of the numbers integers
        average_int = sum_int // i
        i += 1
    
    # New input to restart the intial check, which otherwise would keep carry on because it checks only the first input to enter or exit the cicle 
    n: float = float(input("Write your number here: "))
    
# Final statment and values    
print(f"The average of the numbers integers inserted is equal to: {average_int}\nThe higest number is: {max_n}\nThe lowest number is {min_n}\nThe sum of the integer numbers is: {sum_int}")