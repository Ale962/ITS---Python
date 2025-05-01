# Lesson 3 Exercise 3C-6

'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.

'''

animals: dict = {}
ariah: list = ["aquila", "papagallo", "gufo", "falco", "cigno", "anatra"]
acquah: list = ["balena", "delfino", "squalo", "trota", "salmone", "carpa", "tartaruga", "coccodrillo", "cigno", "anatra"]
terrah: list = ["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo", "gallina", "tacchino", "cigno", "anatra",]
habitats: list = ["aria", "acqua", "terra"]

while True:

    animal: dict = {}

    animal_name: str = input("Write the name of one animal here: ")
    habitat: str = input("Write the habitat of the animal here: ")
    animal["animal"] = animal_name
    animal["habitat"] = habitat


    match (animal["animal"], animal["habitat"]):

        case (name, place) if name in ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]:
            print(f"{name} appartiene alla categoria dei Mammiferi!")
            animal["type"] = "mammifero"
            if place in habitats and (name in ariah and place == "aria") or (name in acquah and place == "acqua") or (name in terrah and place == "terra"):
                print(f"L'animale {name} è un {animal['type']} che può vivere nel habitat {place}")
            else:
                print(f"Non ho mai visto l'animale {name} vivere nell'habitat {place}")

        case (name, place) if name in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
            print(f"{name} appartiene alla categoria dei Rettili!")
            animal["type"] = "rettile"
            if place in habitats and (name in ariah and place == "aria") or (name in acquah and place == "acqua") or (name in terrah and place == "terra"):
                print(f"L'animale {name} è un {animal['type']} che può vivere nel habitat {place}")
            else:
                print(f"Non ho mai visto l'animale {name} vivere nell'habitat {place}")

        case (name, place) if name in ["aquila", "papagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
            print(f"{name} appartiene alla categoria degli Uccelli!")
            animal["type"] = "uccello"
            if place in habitats and (name in ariah and place == "aria") or (name in acquah and place == "acqua") or (name in terrah and place == "terra"):
                print(f"L'animale {name} è un {animal['type']} che può vivere nel habitat {place}")
            else:
                print(f"Non ho mai visto l'animale {name} vivere nell'habitat {place}")
            

        case (name, place) if name in ["squalo", "trota", "salmone", "carpa"]:
            print(f"{name} appartiene alla categoria dei Pesci!")
            animal["type"] = "pesce"
            if place in habitats and (name in ariah and place == "aria") or (name in acquah and place == "acqua") or (name in terrah and place == "terra"):
                print(f"L'animale {name} è un {animal['type']} che può vivere nel habitat {place}")
            else:
                print(f"Non ho mai visto l'animale {name} vivere nell'habitat {place}")

        case _:
            print(f"Non so dire in quale categoria classificare l'animale {animal['animal']}")
            animal["type"] = "unknown"
            print(f"Non ho informazioni riguardo l'habitat {animal['habitat']}")
    
    animals[animal_name] = animal

    add_animal: str = input("Do you want to add a new animal? (Y or N): ")
    if add_animal.upper() == "N":
        break
