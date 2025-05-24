from Shape import Shape

class Circle():
    def __init__(self, r: float):
        super().__init__()
        self.__r: float = r

    def area(self) -> float:
        return 