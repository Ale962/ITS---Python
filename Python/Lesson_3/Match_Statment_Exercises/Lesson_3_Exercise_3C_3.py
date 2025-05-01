# Lesson 3 Exercise 3C-3

'''
Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico

'''

things_list: list = []

for i in range(1, 4):
    
    thing: str = input("Insert something in the list: ")
    things_list.append(thing)
    print(things_list)

match things_list:
    
    case ["penna", "matita", "quaderno"]:
        print("Materiale Scolastico")

    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")

    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")

    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")

    case _:
        print("Categoria sconosciuta")