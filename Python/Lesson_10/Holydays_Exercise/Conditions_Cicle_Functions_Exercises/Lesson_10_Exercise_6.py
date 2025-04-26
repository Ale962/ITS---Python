# Lesson 10 Exercise 6

'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.


Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

Expected Output:

print(hypotenuse(3.0, 4.0)) --> 5.0
print(hypotenuse(8.0, 15.0)) --> 17.0

'''

def hypotenuse(c1: float, c2: float) -> float:

    hypotenuse = ((c1**2) + (c2**2))**(1/2)

    return hypotenuse

print(hypotenuse(3.0, 4.0))
print(hypotenuse(8.0, 15.0))