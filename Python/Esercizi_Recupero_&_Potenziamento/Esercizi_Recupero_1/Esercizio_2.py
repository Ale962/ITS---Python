# Esercizio 2 

def control(x: int, lista: list[int]) -> None:
    pos_x = None
    sum_num_not_x = 0
    repetion: tuple = (x, 0)
    control_list = lista.copy() 
    control_list.append(x)
    for n in control_list:
        if isinstance(n, int):
            continue
        else:
            raise ValueError(f'Number is not an integer')
        
    num, rep = repetion
        
    for n in lista:
        if n == x:
            rep += 1
            if rep == 1:
                pos_x = lista.index(n)
        else:
            sum_num_not_x += n

    print(f'Il numero {x} si ripete {rep} volte, la somma degli altri numeri diversi da {x} è {sum_num_not_x}, la prima posizione in cui si incontra {x} è {pos_x}.')


if __name__ == '__main__':
    list1 = [7, 5, 1, 3, 3, 3, 11, 2, 3, 3, 0]

    control(3, list1)