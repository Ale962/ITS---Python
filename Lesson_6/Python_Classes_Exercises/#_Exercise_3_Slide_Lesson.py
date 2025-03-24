'''
Exercise 3 (Folder 9 ex_3.py)
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal
'''

class animal:
    def __init__(self, name_animal: str, legs: int):
        self.name_animal = name_animal
        self.legs = legs

    def displayanimalinfo(self):
        print(f"The name of the animal is {self.name_animal}, it has {self.legs} legs")

    def setLegs(self, a:int):
        self.legs = a

    def getLegs(self):
        print(self.legs)


giraffe = animal("Giraffe", 3)
lion = animal("Lion", 2)
giraffe.displayanimalinfo()
lion.displayanimalinfo()
giraffe.setLegs(4)
lion.setLegs(4)
giraffe.displayanimalinfo()
lion.displayanimalinfo()
giraffe.getLegs()
lion.getLegs()