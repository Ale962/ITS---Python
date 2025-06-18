# Exercise 8.A
from __future__ import annotations
class Frazione:

    def __init__(self, numeratore, denominatore):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, numeratore = 13) -> None:
        if isinstance(numeratore, int):
            self.__numeratore = numeratore
        else:
            numeratore = 13
            self.__numeratore = numeratore

    def set_denominatore(self, denominatore = 5) -> None:
        if denominatore == 0:
            denominatore = 5
        
        if isinstance(denominatore, int):
            self.__denominatore = denominatore
        else:
            denominatore = 5
            self.__denominatore = denominatore

    def get_numeratore(self) -> int:
        return self.__numeratore
    
    def get_denominatore(self) -> int:
        return self.__denominatore
    
    def value(self) -> float:
        value = self.__numeratore / self.__denominatore
        return round(value, 3)
    
    def __str__(self) -> str:
        return f'La frazione con il numeratore {self.__numeratore} e denominatore {self.__denominatore}, ha come risultato {self.value()}'
    

def mcd(x: int, y: int) -> int:
    list_div: list[int] = []
    max_div = 1
    max_n = max(x, y)
    max_n = int(max_n)

    for i in range(2, max_n):
        if x % i == 0 and y % i == 0:
            list_div.append(i)
    
    if list_div:
        max_div = max(list_div)
    
    return max_div



    '''
    for i in range(2, x+1):
        frazione: Frazione = Frazione(x, i)
        result = frazione.value()
        if result == 0:
            x_div.append(result)

    for z in range(2, z+1):
        frazione: Frazione = Frazione(y, z)
        result = frazione.value()
        if result == 0:
            y_div.append(result)

    for xd in x_div:
        for yd in y_div:
            if xd == yd:
                current_value = xd
                if current_value > max_div:
                    max_div = current_value
    
    return max_div
    '''

def semplifica(frazioni: list[Frazione]) -> list[Frazione]:
    frazioni_irriducibilie: list[Frazione] = []

    for f in frazioni:
        numeratore = f.get_numeratore()
        denominatore = f.get_denominatore()
        mincomdiv = mcd(numeratore, denominatore)
        if mincomdiv == 1:
            frazioni_irriducibilie.append(f)
        else:
            while True:
                if mincomdiv != 1:
                    numeratore //= mincomdiv
                    denominatore //= mincomdiv
                    mincomdiv = mcd(numeratore, denominatore)
                else:
                    frazioni_irriducibilie.append(Frazione(numeratore, denominatore))
                    break

    return frazioni_irriducibilie

def fractionCompare(frazioni: list[Frazione], frazioni_semplificate: list[Frazione]) -> None:
    for f, fs in zip(frazioni, frazioni_semplificate):
        if f.value() == fs.value():
            print('---------------'*3)
            print(f'Valore frazione originale {f} è {f.value()} --- Valore frazione semplificata {fs} è {fs.value()}')
            print('---------------'*3)

if __name__ == '__main__':
    l: list[Frazione] = [
        Frazione(2.5, 0),
        Frazione(1, 2),
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15)
    ]

    ls = semplifica(l)
    print(fractionCompare(l, ls))