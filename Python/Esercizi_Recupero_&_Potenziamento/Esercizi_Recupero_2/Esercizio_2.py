# Esercizio 2

def proDict() -> dict[tuple, int]:
    d: dict[tuple, int] = {}
    for x in range(0, 101):
        for y in range(2, 89, 2):
            d[(x, y)] = x*y
    return d

if  __name__ == '__main__':
    print(proDict())