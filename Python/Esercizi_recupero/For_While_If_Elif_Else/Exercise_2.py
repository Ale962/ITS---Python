# Exwercise 2

'''
2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.

'''

def multiply(list1: list[int|float], threshold: int) -> int|float:

    result = 1

    for x in range(min(list1), max(list1)+1):
        if x < threshold:
            result *= abs(x)

    return result

if __name__ == '__main__':
    list1 = list(range(1, 56))
    print(multiply(list1, 20))