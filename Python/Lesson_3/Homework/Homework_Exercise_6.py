# Homework Exercise 6

'''
Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.
'''

# Variables
n1: int = int(input("Insert the first number here: "))
n2: int = int(input("Insert the second number here: "))
numbers: list = []
product: int = 1

# (sorry to use if instead of match statment, python online doesn't recognise match function and VS is not working as intended on my pc)
# First case, n1 < n2
if n1 < n2:
    
    # Setting up a list of numbers that start from n1 to n2
    numbers: list = range(n1, n2+1)
    
    # Calculating the product
    for number in numbers:
        product *= number
    
    # Result    
    print(f"The product of the numbers beetwen {n1} and {n2} is: {product}")
    
    
# Second case, n2 < n1        
if n2 < n1:
    
    # Setting up a list of numbers that start from n2 to n1
    numbers: list = range(n2, n1+1)
    
    # Calculating the product
    for number in numbers:
        product *= number
    
    # Result    
    print(f"The product of the numbers beetwen {n2} and {n1} is: {product}")