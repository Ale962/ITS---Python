# Lesson 13 Exercise 7

'''
Esercizio 7.

Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi3 una produttoria definita come segue:
Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  

Calcolare il valore della produttoria Pi3 se n = 5.

'''

def Pi3(n):

    n = int(abs(n))

    if n <=1:
        return 1
    else:
        return (n**3) * Pi3(n-1)
    
print(Pi3(5))