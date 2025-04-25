# Progetto: Realizzazione e gestione dei corsi ITS PARTE 2

### Class Person ###

class Person:

    def __init__(self, name: str, surname: str, cf: str, age: int ):
        self.set_name(name)
        self.set_surname(surname)
        self.set_cf(cf)
        self.set_age(age)

    def set_name(self, name) -> None:
        self.name = name

    def set_surname(self, surname) -> None:
        self.surname = surname

    def set_cf(self, cf) -> None:
        self.cf = cf 

    def set_age(self, age) -> None:
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_surname(self) -> str:
        return self.surname

    def get_cf(self) -> str:
        return self.cf

    def get_age(self) -> int:
        return self.age
    

class Student(Person):

    def __init__(self, name, surname, cf, age):

        super().__init__(name, surname, cf, age)

        self.group = None

    def set_group(self, group):
        self.group = group

    def get_group(self):
        return self.group


class Lecturer(Person):

    def __init__(self, name, surname, cf, age):
        super().__init__(name, surname, cf, age)


class Group:

    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []

    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):

        students = len(self.students)
        limit_lecturers = 0

        if students < 10:
            limit_lecturers = 1

        else:
            limit_lecturers = students // 10

        return limit_lecturers
    
    def add_student(self, student: Student):
        
        if len(self.students) < self.limit:
            self.students.append(student)

    def add_lecturer(self, lecturer: Lecturer):

        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)