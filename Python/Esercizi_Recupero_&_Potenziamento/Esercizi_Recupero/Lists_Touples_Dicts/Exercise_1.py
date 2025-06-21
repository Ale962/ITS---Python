# Exercise 1

'''
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.

'''

def converter(list: list[tuple]) -> dict:

    newdict: dict = {}

    for key, value in list:
        if key in newdict:
            newdict[key] += value
        else:
            newdict[key] = value

    return newdict


if __name__ == '__main__':

    list1: list[tuple] = [('Lazio', 3), ('Lazio', 3), ('Juventus', 2)]

    print(converter(list1))