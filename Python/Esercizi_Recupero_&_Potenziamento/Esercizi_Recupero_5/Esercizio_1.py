import random
import math

# Genera una matrice n*n con numeri random tra 0 e 13
def genera(n: int) -> list[list[int]]:
    mat: list[list[int]] = []
    for r in range(n):
        row: list[int] = []
        for c in range(n):
            while True:
                x: int = random.randint(0,13)
                if len(row) == 0 or x != row[0]: # controllo che il primo elemento della riga sia diverso dall'attuale valore e se diverso lo tengo
                    row.append(x)
                    break
        mat.append(row)
    return mat

# Printa la matrice con un minimo di 5 spazi
def printMAT(mat: list[list[int]]) -> None:
    for r in mat:
        string: str = ''
        for x in r:
            string += f'{x:5}' # questo sistema permette di avere 5 spazi per ogni elemento a cominciare da sinistra esempio 5 verrà printato come '    5'
        print(string)

# Calcola i carichi, i carichi corrispondo alla somma degli elementi della row indicata e della colonna indicata
def calcoloCarico(mat: list[list[int]], r: int, c: int) -> int:
    sum_r = sum(mat[r])
    sum_c = 0
    for row in mat:
        sum_c += row[c]
    k = sum_r - sum_c
    return k

# Calcolo i carichi nulli (uguali a 0) e li salvo in una lista
def caricoNullo(mat: list[list[int]]) -> list[tuple[int, int]]:
    carichi_nulli: list[tuple[int, int]] = []
    k = len(mat)
    for r, row in enumerate(mat): # uso enumerate per ottenere una tupla che mi rida indice della riga e riga unumerate(list) --> (indice elemento, elemento)
        for c in range(k):
            result = calcoloCarico(mat, r, c)
            if result == 0:
                t: tuple[int, int] = (r, c) # mi salvo la tupla con i valori che mi danno 0 in calcoloCarico()
                carichi_nulli.append(t)
    return carichi_nulli

# Calcolo il carico massimo e torno il valore printato e la coppia di valori che hanno portato al massimo
def caricoMax(mat: list[list[int]]) -> tuple[int, int]:
    max = -math.inf
    k = len(mat)
    for r, row in enumerate(mat):
        for c in range(k):
            result = calcoloCarico(mat, r, c)
            if result > max:
                max = result
                max_value: tuple[int, int] = (r, c)
    print(f"Il valore massimo è uguale è {max}")
    return max_value

# Calcolo il carico minimo e torno il valore printato e la coppia di valori che hanno portato al minimo
def caricoMin(mat: list[list[int]]) -> tuple[int, int]:
    min = math.inf
    k = len(mat)
    for r, row in enumerate(mat):
        for c in range(k):
            result = calcoloCarico(mat, r, c)
            if result < min:
                min = result
                min_value: tuple[int, int] = (r, c)
    print(f"Il valore minimo è uguale è {min}")
    return min_value 

if __name__ == '__main__':

    mat1 = genera(5)
    printMAT(mat1)
    print(caricoNullo(mat1))
    print(caricoMax(mat1))
    print(caricoMin(mat1))
    rmax, cmax = caricoMax(mat1)
    print(f'Prova max {rmax}, {cmax}')
    rmin, cmin = caricoMin(mat1)
    print(f'Prova min {rmin}, {cmin}')