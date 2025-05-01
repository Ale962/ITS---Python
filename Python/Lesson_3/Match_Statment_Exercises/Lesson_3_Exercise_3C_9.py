# Lesson 3 Exercise 3C-9

'''
Esercizio 3C-9. Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla. Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."

Expected Output:

Inserisci la coordinata X: 0
Inserisci la coordinata Y: 0
Output: Il punto (0,0) si trova nell'origine.

- - - - - - - - - - - - - - - - - - - - - -

Inserisci la coordinata X: 3
Inserisci la coordinata Y: 5
Output: Il punto (3,5) si trova nel primo quadrante.

- - - - - - - - - - - - - - - - - - - - - - - - -

Inserisci la coordinata X: 4
Inserisci la coordinata Y: 0
Output: Il punto (4,0) si trova sull'asse X.

'''

points: dict = {}
i = 1

while True:

    point: dict = {}

    x: int = int(input("Insert x coordinates here: "))
    y: int = int(input("Insert y coordinates here: "))

    point["x"] = x
    point["y"] = y
    points[i] = point

    match (x, y):

        case (0 ,0):
            print("The point is at the origin.")

        case (x, 0):
            print("The point is on the X axis.")

        case (0, y):
            print("The point is on the Y axis.")

        case (x, y) if x > 0 and y > 0:
            print("The point is in the first quadrant.")

        case (x, y) if x < 0 and y > 0:
            print("The point is in the second quadrant.")

        case (x, y) if x < 0 and y < 0:
            print("The point is in the third quadrant.")

        case (x, y) if x > 0 and y < 0:
            print("The point is in the fourth quadrant.")

    i += 1

    add_new_point: str = input("Want to add a new point? (Y or N): ")

    if add_new_point.upper() == "N":
        break