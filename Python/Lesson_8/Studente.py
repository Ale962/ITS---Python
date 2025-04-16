from Persona import Person


class Student(Person):

    def __init__(self, name:str, lastname:str, age:int, matricola:str ):

        super().__init__(name, lastname, age)

        self.setMatricola(matricola)

    def setMatricola(self, matricola) -> None:

        if matricola:
            self.matricola = matricola
        else:
            print("**Can't have a void string as value**")

    def getMatricola(self) -> str:
        return self.matricola
    
    def __str__(self) -> str:
        return f"\nName: {self.getname()}\nLastname: {self.getlastname()}\nMatricola: {self.getMatricola()}"
    