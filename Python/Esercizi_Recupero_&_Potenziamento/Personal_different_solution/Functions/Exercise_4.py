# Exercise 4

'''
Somma delle Diagonali di una Matrice (Quadrata o
Rettangolare)
Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:
1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).
2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).
Requisiti:
● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.
Esempi:
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15
sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15

'''
import random

def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    sum_dia = 0
    index = 0

    '''
    for l in range(len(matrix)):
        sum_dia += matrix[i][i]
    '''

    for l in matrix:
        if len(l) > index:
            sum_dia += l[index]
            index += 1
        else:
            break
    return sum_dia

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    sum_dia = 0
    index = len(matrix[0]) -1
    for l in matrix:
        if len(l) > index:
            sum_dia += l[index]
            index -= 1
        else:
            break
    return sum_dia

if __name__ == '__main__':
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(sum_primary_diagonal(mat1))    
    print(sum_secondary_diagonal(mat1))  

    mat2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]

    print(sum_primary_diagonal(mat2))    
    print(sum_secondary_diagonal(mat2))  