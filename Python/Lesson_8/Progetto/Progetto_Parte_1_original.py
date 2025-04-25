# Progetto: Realizzazione e gestione dei corsi ITS PARTE 1

### Class Room ###

class Room:

    def __init__(self, id: str, floor: int, seats: int ):
        self.setId(id)
        self.setFloor(floor)
        self.setSeats(seats)

    def setId(self, id) -> None:
        self.__id = id

    def setFloor(self, floor) -> None:
        self.__floor = floor

    def setSeats(self, seats) -> None:
        self.__seats = seats
        self.__area = seats * 2

    def getId(self) -> str:
        return self.__id

    def getFloor(self) -> int:
        return self.__floor

    def getSeats(self) -> int:
        return self.__seats

    def getArea(self) -> int:
        return self.__area
    

class Building:

    def __init__(self, name: str, address: str, floors: int):
        self.setName(name)
        self.setAddress(address)
        self.setFloors(floors)
        self.__rooms: list[Room] = []

    def setName(self, name) -> None:
        self.__name = name

    def setAddress(self, address) -> None:
        self.__address = address

    def setFloors(self, floors) -> None:
        self.__floors = floors

    def addRoom(self, room: Room) -> None:
        if room.__floor in range (0, self.__floors + 1):
            self.__rooms.append(room)

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def getFloors(self) -> int:
        return self.__floors

    def getRooms(self) -> int:
        return self.__rooms
    
    def area(self):
        self.__areabui = 0

        for room in self.__rooms:
            self.__areabui += room.getArea()

        return self.__areabui