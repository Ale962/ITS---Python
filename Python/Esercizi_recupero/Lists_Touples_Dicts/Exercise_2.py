# Exercise 2

'''
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.

'''

def evenodd(list1: list[int|float]) -> dict:

    new_dict: dict[str, list[int|float]] = {'positive': [], 'negative': []}

    for x in list1:
        if x > 0:
            new_dict['positive'].append(x)
        else:
            new_dict['negative'].append(x)
    return new_dict


if __name__ == '__main__':

    list_numbers: list[int] = [2, -5, 9, 8, 12, -97]

    print(evenodd(list_numbers))