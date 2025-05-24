from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass