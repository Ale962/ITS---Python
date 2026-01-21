'''Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.'''

def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice

    dict_even_odd = {
        'pari': [filter(lambda x : x % 2 == 0, lista)],
        'dispari': [filter(lambda x : x % 2 != 0, lista)]
        }


    # alternative con ciclo for
    '''
    for x in lista:

        if x % 2 == 0:
            dict_even_odd['pari'].append(x)
        else:
            dict_even_odd['dispari'].append(x)
    '''
    
    # alternativa con map
    dict_even_odd_2 = {
        'pari': [map(lambda x : x if x % 2 == 0 else '', lista)], 
        'dispari': [map(lambda x : x if x % 2 != 0 else '', lista)]
        }

    # alternativa con comprehension
    dict_even_odd_3 = {
        'pari': [x for x in lista if x % 2 == 0],
        'dispari': [x for x in lista if x % 2 == 0]
    }

    return dict_even_odd