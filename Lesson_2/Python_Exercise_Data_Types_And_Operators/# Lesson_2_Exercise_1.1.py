# Lesson 2 Exercise 1.1

'''1-1. Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare 1.0/x memorizzare il risultato nella variabile y.
    Visualizzare il valore di x, y e il prodotto tra x e y.
    Sottrarre x dal prodotto tra x e y e mostrarne il risultato.
'''

x:float = 4.25

y:float = 1.0 / x

print(f"Il valore di x è: {x} \nIl valore di y è: {y:.2f}")

print(f"\nIl prodotto tra x e y vale: {x*y}")

# modo 1
print(f"\nx*y-x: {x*y-x}") 

# modo 2
z:float = x*y
print(f"\nz-x: {z-x}")