# Lesson 7 Exercise on Functions 5

'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.

Expected Output:

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) --> {'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) --> {}

'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    
    prodotti_scontati: dict = {}

    for key, value in prodotti.items():

        if value > 20:
            value *= 0.9
            prodotti_scontati[key] = value

        else:
            continue
    
    return prodotti_scontati

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))