# Exercise 2.b

'''
Creare un funzione recursiva che calcoli il fattoriale di un dato numero

'''


def factoriale(n: int):
    if n < 0:
        raise ValueError('The number must be positive')

    if n == 1:
        return 1
    
    else:
        return n * factoriale(n-1)
    

if __name__ == '__main__':

    print(factoriale(3))