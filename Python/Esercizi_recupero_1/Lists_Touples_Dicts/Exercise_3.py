# Exercise 3 

'''
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.

'''

def lessthen50(dict1: dict[str, float]) -> dict[str, float]:

    dict_filter: dict[str, float] = {}

    for key, value in dict1.items():
        if value < 50:
            value *= 1.10
            value_round = round(value, 2)
            dict_filter[key] = value_round

    return dict_filter

if __name__ == '__main__':

    prodotti: dict[str, float] = {'pollo': 25.00, 'televisore': 149.99, 'termos': 10.75, 'vino': 75.99}

    print(lessthen50(prodotti))