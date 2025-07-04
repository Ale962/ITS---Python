def baricentro(v: list[int]) -> int|None:
    sum_left = 0
    sum_right = 0
    for i in range(len(v)):
        sum_left = sum(v[:i])
        sum_right = sum(v[i+1:])
        if sum_left == sum_right:
            return i
    return None
    
def printResult(v: list[int]) -> None:
    result = baricentro(v)
    if result != None:
        print(f"Esiste il baricentro del vettore {v} ed è dato dall'indice i ={result}")
    else:
        print(f"Il baricentro del vettore {v} non esiste!")

def baricentroOttimizzato(v: list[int]) -> int|None:
    sum_elements = sum(v)
    sum_left = 0
    for i in range(len(v)):
        sum_right = sum_elements - sum_left - v[i]
        if sum_right == sum_left:
            return i
        sum_left += v[i]
    return None

if __name__ == '__main__':
    v1 = [1, 2, 3, 2, 5, 2, 1]
    v2 = [2, 0, -1, 4, 6, 3, -1]
    print()
    printResult(v1)
    print()
    printResult(v2)
    print()
    print(f'Il baricentro calcolato con la funzione baricentro ottimizzato del primo vettore è {baricentroOttimizzato(v1)}')
    print()
    print(f'Il baricentro calcolato con la funzione baricentro ottimizzato del secondo vettore è {baricentroOttimizzato(v2)}')