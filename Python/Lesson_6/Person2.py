# Person 2

class Person:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    def displaydata(self) -> None:
        print(f"Name: {self.name}\nLastname: {self.lastname}\nAge: {self.age}")

    # Function that allow to create a valure for self.name

    def setname(self, name: str) -> None:

        self.name = name

    # Function that allow to create a valure for self.lastname

    def setlastname(self, lastname: str) -> None:

        self.lastname = lastname

    # Function that allow to create a valure for self.lastname

    def setage(self, age: int)-> None:

        if age < 0 or age > 150:
            self.age = 0

        else:    
            self.age = age

    def getname(self) -> str:

        return self.name
    
    
    def getlastname(self) -> str:

        return self.lastname
    
    def getage(self) -> int:

        return self.age
