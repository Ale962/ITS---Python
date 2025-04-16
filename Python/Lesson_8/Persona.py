# Classes

class Person:
    def __init__(self, name: str, lastname: str, age: int):
        self.setname(name)
        self.setlastname(lastname)
        self.setage(age)

    #
    # Metod that make you possible to call all the attribute in this string with the simple print comand of the class

    def __str__(self) -> str:
        return f"Name {self.getname()}\nLastname: {self.getlastname()}\nAge: {self.getage()}"
    
    # Function that allow to create a valure for self.name

    def setname(self, name: str) -> None:
            
        if name:
            self.name = name
        else:
            print("**Can't leave a void string as name**")

    # Function that allow to create a valure for self.lastname

    def setlastname(self, lastname: str) -> None:

        if lastname:
            self.lastname = lastname
        else:
            print("**Can't leave a void string as name**")

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
