# Lesson 7 Exercise on Functions 4

'''

Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

Expected Output:

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])) --> {'Alice': [90, 85], 'Bob': [75]}
print(aggrega_voti([])) --> {}

'''

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:

    d2: dict = {}

    for x in voti:

        nome = x["nome"]
        voto = x["voto"]
        
        if nome in d2:
            d2[nome].append(voto)
        else:
            d2[nome]=[voto]

    return d2

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([]))