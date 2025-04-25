# Progetto: Realizzazione e gestione dei corsi ITS PARTE 1

### Class Room ###

class Room:

    def __init__(self, id: str, floor: int, seats: int ):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def set_id(self, id) -> None:
        self.id = id

    def set_floor(self, floor) -> None:
        self.floor = floor

    def set_seats(self, seats) -> None:
        self.seats = seats
        self.area = seats * 2 

    def get_id(self) -> str:
        return self.id

    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats

    def get_area(self) -> int:
        return self.area
    

### Class Building ###

class Building:

    def __init__(self, name: str, address: str, floors: tuple):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []

    def set_name(self, name) -> None:
        self.name = name

    def set_address(self, address) -> None:
        self.address = address

    def set_floors(self, floors) -> None:
        self.floors = floors

    def add_room(self, room: Room) ->  None:
        if room.floor in range (min(self.floors), max(self.floors) + 1):
            if not any(r.get_id() == room.get_id() for r in self.rooms):
                self.rooms.append(room)


    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        return self.address

    def get_floors(self) -> int:
        return self.floors

    def get_rooms(self) -> list:
        return self.rooms
    
    def area(self):
        self.areabui = 0

        for room in self.rooms:
            self.areabui += room.get_area()

        return self.areabui