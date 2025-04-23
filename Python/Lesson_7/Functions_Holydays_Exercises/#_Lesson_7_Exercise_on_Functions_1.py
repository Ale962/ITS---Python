# Lesson 7 Exercise on Functions 1

'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.

Expected output:

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3})) --> {1: 'a', 2: 'b', 3: 'c'}
print(inverti_mappa({})) --> {}

'''

def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:

    inverted: dict = {}

    for key, value in dizionario.items():

        if value in inverted:
            continue
        else:
            inverted[value] = key

    return inverted