from Persona import Person
from Studente import Student

p: Person = Person("Alessio", "Caico", 29)

print(p)


studente1: Student = Student("Rachele", "Corsi", 26, "52523")

print(studente1)

if isinstance(studente1, Student):
    print("\nstudente1 is an object of the class Student")

if isinstance(studente1, Person):
    print("\nstudente1 is an object of the class Person")

if isinstance(p, Person):
    print("\np is an object of the class Person")

if isinstance(p, Student):
    print("\np is an object of the class Person and an object of the class Student")
else:
    print("\np is an object of the class Person but it is not an object of the class Student")

if issubclass(Student, Person):
    print("\nStudent is a subclass of the class Person")