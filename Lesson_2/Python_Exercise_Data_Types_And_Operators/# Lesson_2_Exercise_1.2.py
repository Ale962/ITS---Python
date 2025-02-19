# Lesson 2 Exercise 1.1

'''1-2. Si scriva un programma che dimostri le funzionalità dell'operatore % effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare x%2.0 e memorizzare il risultato nella variabile y.
    Visualizzare in maniera distinta x e y.
'''

x:float = 9.85

y:float = x % 2.0

print(f"Il valore di x è: {x}\nIl valore di y è: {y:.2f}")

x:float = -9.85

print(f"Il valore di x è: {x}\nIl valore di y è: {y:.2f}")