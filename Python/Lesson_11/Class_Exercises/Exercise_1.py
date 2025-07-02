from __future__ import annotations
from datetime import time
from typing import Any

class Film:
    def __init__(self, name: str, duration: time):
        self.setName(name)
        self.setDuration(duration)

    def setName(self, name: str) -> None:
        self.__name = name

    def setDuration(self, duration: time) -> None:
        self.__duration = duration

    def name(self) -> str:
        return self.__name
    
    def duration(self) -> time:
        return self.__duration
    
    def __hash__(self):
        return hash((self.name(), self.duration()))
    
    def __eq__(self, other: Any):
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        return (self.name(), self.duration()) == (other.name(), other.duration())
    
    def __repr__(self):
        return f"{self.name()}"
    
class Sala:

    def __init__(self, id: str, sits_num: int, sits_prenotated: int = 0, film: Film|None = None):
        self.setID(id)
        if film:
            self.setFilm(film)
        self.setSitsNum(sits_num)
        self.__sits_prenotated = sits_prenotated

    def setID(self, id: str) -> None:
        self.__id = id

    def setFilm(self, film: Film) -> None:
        self.__film = film

    def setSitsNum(self, sits_num: int) -> None:
        self.__sits_num = sits_num

    def setSitsPrenotated(self, sits_prenotated: int) -> None:
        self.__sits_prenotated = sits_prenotated

    def prenote_sits(self, s = int) -> None:
        available = self.sits_aviable()
        if s > available:
                print('The sits aviable are less then the number of sits being prenotated, please restart process')
        elif s <= available:
            self.__sits_prenotated += s
            print('The sit/s have been prenoted')
            print(f'{s} sits for {self.film()} reserved')
        else:
            print(f'Cannot prentate sits fof {self.film()}')
            print('No more sits aviable')

    def id(self) -> str:
        return self.__id
    
    def film(self) -> Film:
        return self.__film
    
    def sits_num(self) -> int:
        return self.__sits_num
    
    def sits_prenotated(self) -> int:
        return self.__sits_prenotated
    
    def sits_aviable(self) -> int:
        aviable = self.sits_num() - self.sits_prenotated()
        return aviable
    
    def __hash__(self):
        return hash((self.id()))
    
    def __eq__(self, other: Any):
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        return (self.id()) == (other.id())
    
    def __repr__(self):
        if self.film() != None:
            return f"The hall with id {self.id()} which has in programm {self.film()}, there are {self.sits_aviable()} sits aviable"
        else:
            return f"The hall with id {self.id()} and there are {self.sits_aviable()} sits aviable"

class Cinema:

    def __init__(self, name: str, sala: Sala|None = None, film: Film|None = None):
        self.__sale: set[Sala] = set()
        self.setName(name)
        if sala:
            self.add_sala(sala)
            if film:
                sala.setFilm(film)

    def setName(self, name: str) -> None:
        self.__name = name

    def add_sala(self, sala: Sala) -> None:
        if sala in self.__sale:
            print('An hall with the same ID is already present, cannot add two halls with the same ID')
        else:    
            self.__sale.add(sala)

    def prenote_film(self, film: Film, sits_num: int) -> None:
        for s in self.__sale:
            if s.film() == film:
                if s.sits_aviable() > 0:
                    s.prenote_sits(sits_num)
                    break
            else:
                print(f'The film {film} is not being reproduced in this cinema')

    def sale(self) -> None|frozenset[Sala]:
        if self.__sale:
            for s in self.__sale:
                print(s)
        return frozenset(self.__sale)

    def name(self) -> str:
        return self.__name
    
    def __hash__(self):
        return hash((self.name()))
    
    def __eq__(self, other):
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        return (self.name()) == (other.name())

    def __repr__(self):
        return f"Cinema: {self.name()}"
    
if __name__ == '__main__':

    # Create some films
    film1 = Film("Inception", time(hour=2, minute=28))
    film2 = Film("Interstellar", time(hour=2, minute=49))

    # Create salas
    sala1 = Sala("A1", 50, film=film1)
    sala2 = Sala("B1", 30)

    # Create a cinema
    cinema = Cinema("CineRoma", sala1)

    # Add another sala to the cinema
    cinema.add_sala(sala2)
    sala2.setFilm(film2)

    # Print cinema details
    print(cinema)

    # Show all salas
    cinema.sale()

    # Try booking seats
    cinema.prenote_film(film1, 20)
    cinema.prenote_film(film1, 40)  # Should print an error due to overbooking
    cinema.prenote_film(film2, 10)

    # Print salas again to see updated sits
    cinema.sale()