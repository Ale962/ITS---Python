

class Persona:

    def __init__(self, first_name: str, last_name: str, age: int = 0):
        self.__setName(first_name)
        self.__setLastName(last_name)
        self.__setAge(age)

    def __setName(self, first_name: str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print('Il nome inserito non è una stringa')

    def __setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print('Il cognome inserito non è una stringa')

    def __setAge(self, age: int):
        if isinstance(age, int):
            self.__age = age
        else:
            self.__age = None
            print("L'età inserita non è un numero")

    def getName(self) -> str:
        return self.__first_name
    
    def getLastName(self) -> str:
        return self.__last_name
    
    def getAge(self) -> int:
        return self.__age
    
    def greet(self) -> str:
        return f'Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!'