from __future__ import annotations

class Documento:

    def __init__(self, text: str):
        self.setText(text)

    def setText(self, text:str):
        self.__text = text

    def getText(self) -> str:
        return self.__text
    
    def isInText(self, word: str) -> bool:
        if word in self.getText():
            return True
        else:
            return False
        
    def __repr__(self):
        return f'{self.getText()}'
        
class Email(Documento):

    def __init__(self, text, mittente: str, destinatario: str, titolo_messaggio: str):
        super().__init__(text)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitoloMessaggio(titolo_messaggio)

    def setMittente(self, mittente: str) -> None:
        self.__mittente = mittente

    def setDestinatario(self, destinatario: str) -> None:
        self.__destinatario = destinatario

    def setTitoloMessaggio(self, titolo_messaggio: str) -> None:
        self.__titolo_messaggio = titolo_messaggio

    def getMittente(self) -> str:
        return self.__mittente
    
    def getDestinatario(self) -> str:
        return self.__destinatario
    
    def getTitoloMessaggio(self) -> str:
        return self.__titolo_messaggio
    
    def getText(self) -> str:
        return f'Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitoloMessaggio()}\nMessaggio: {super().getText()}'
    
    def __repr__(self):
        return f'{self.getText()}'
    
    def WriteToFile(self, percorso_file: str) -> None:
        with open(percorso_file, 'a') as file:
            file.write(self.getText())


class File(Documento):

    def __init__(self, percorso_file: str):
        self.setPercorsoFile(percorso_file)
        super().__init__(self.leggiTestoDaFile())

    def setPercorsoFile(self, percorso_file: str) -> None:
        self.__percorso_file = percorso_file

    def getPercorsoFile(self) -> str:
        return self.__percorso_file
    
    def leggiTestoDaFile(self) -> str|None:
        with open(self.getPercorsoFile(), 'r') as file:
            return file.readlines()
        
    def getText(self) -> str:
        return f'Percorso: {self.getPercorsoFile()}\nConenuto: {super().getText()}'