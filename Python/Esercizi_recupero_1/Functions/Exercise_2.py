# Binary Exercise

'''
Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False

'''

def BinaryResearch(numbers: list[int], number: int, low: int = 0, high: int = None) -> bool:
    num_sort: list[int] = sorted(set(numbers))
    high = len(num_sort)
    while low < high:
        mid = (low + high)//2
        midnumber = num_sort[mid]
        if midnumber > number:
            high = mid
        elif midnumber < number: 
            low = mid + 1
        else: 
            return True

    return False