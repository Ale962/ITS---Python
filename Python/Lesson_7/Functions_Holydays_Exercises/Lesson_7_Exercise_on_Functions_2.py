# Lesson 7 Exercise on Functions 2

'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

Expected Output:

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)])) --> {'a': [1, 3], 'b': [2]}
print(lista_a_dizionario([])) --> {}

'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:

    dictionary: dict = {}

    dict(tuples)

    for key, value in tuples:

        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    return dictionary

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))