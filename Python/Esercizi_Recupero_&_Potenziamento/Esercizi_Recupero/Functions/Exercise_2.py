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

def BinaryResearchRecursive(numbers: list[int], num: int):
    list_sorted = sorted(set(numbers))
    mid = len(list_sorted)//2

    if list_sorted[mid] == num:
        print('Number found!')
        return True
    elif len(list_sorted) == 1:
        print('Number not found!')
        return False
    elif list_sorted[mid] > num:
        BinaryResearchRecursive(list_sorted[:mid], num)
    elif list_sorted[mid] < num:
        BinaryResearchRecursive(list_sorted[mid:], num)


'''
lista1 = [1, 5, 6. 9, 11]

print(BinaryResearch(lista1, 6))

low # lowest index = 0

high = None --> 5 perchè len(lista) è uguale a 5

siccome 0 < 5:

    # primo ciclo
    mid = (0+5) // 2 --> 2
    midnumber = lista1[mid] --> 5

    se 5 è minore di 6:
        low (0) --> mid (2)+1 --> low = 3
    
    
    # secondo ciclo
    siccome 3 < 5:

        mid = (3+5)//2 --> 4
        midnumber = lista1[mid] --> 11

        se 1 < 3:
            low(0) --> mid(1)+1 --> 2

        # terzo ciclo:
        è ancora 2 < 2:?


Return False
'''