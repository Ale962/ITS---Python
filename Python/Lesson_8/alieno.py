

class Alieno:

    '''
    della classe alieno ci interessa sapere la galassia di provenienza
    self.galaxy:str
    '''

    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) -> None:

        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia non può essere una stringa vuota!")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print(f"\nG!!tgfuf##a8c(=CUC)@\n")

    def __str__(self) -> str:
        return f"\nL'alieno viene dalla Galassia {self.getGalaxy()}!\n"
    

