# Progetto: Realizzazione e gestione dei corsi ITS PARTE 3

from Progetto_Parte_2 import Group
from Progetto_Parte_2 import Student

class Course:

    def __init__(self, name: str):
        self.name = name
        self.groups : list[Group] = []

    def set_name(self, name: str):
        self.name = name

    def register(self, student: Student):

        for g in self.groups:

            if len(g.get_students()) < g.get_limit():
                g.add_student(student)

    def get_name(self):
        return self.name

    def get_groups(self):
        return self.groups
    
    def add_group(self, group: Group):
        self.groups.append(group)