# Lesson 7 Exercise on Functions 3

'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

Expected Output:

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) --> [1, 3, 4]
print(rimuovi_elementi([], {2: 1})) --> []

'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    clean_list: list = []

    for key, value in da_rimuovere.items():
        
        i = 1
        
        for x in lista:
            
            if x == key:
                if i <= value:
                    i+=1
                    continue
                else:
                    clean_list.append(x)

            else:
                clean_list.append(x)

    return clean_list

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1}))