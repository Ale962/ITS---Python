# Classes

class Person:
    def __init__(self, name: str, lastname: str, age: int):
        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age

    # Function of the class person that print the attributes of the person

    def displaydata(self) -> None:
        print(f"Name: {self.name}\nLastname: {self.lastname}\nAge: {self.age}")