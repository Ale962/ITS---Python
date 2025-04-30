from abc import ABC, abstractmethod

class formaGenerica(ABC):
    
    @abstractmethod
    def draw(seld) -> None:
        pass

    def setShape(self, shape: str) -> None:
        if shape:
            self.shape = shape
        else:
            print("Errore1 Specificare uno shape!")

    def getShape(self) -> str:
        return self.shape