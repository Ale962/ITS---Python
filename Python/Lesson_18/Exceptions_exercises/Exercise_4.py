# Lesson 18 Exercise 4

'''
Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string.

'''

import re

class DatabaseDates:
    def __init__(self):
        self.__database: dict = {}

    def __is_valid_date(self, date):
        return bool(re.fullmatch(r"(0[1-9]|[1-2][0-9]|3[0-1])\.(0[1-9]|1[0-2])\.\d{4}", date))

    def __get_next_available_index(self):
        for i in range(len(self.__database) + 1):
            if i not in self.__database:
                return i

    def addDate(self, date):
        if not self.__is_valid_date(date):
            raise ValueError("Date format not recognized. Use gg.mm.aaaa")
        i = self.__get_next_available_index()
        self.__database[i] = date
        return i

    def removeDate(self, i): 
        if i in self.__database:
            del self.__database[i]
        else:
            raise KeyError("No such date index.")

    def modifyDate(self, i, date):
        if not self.__is_valid_date(date):
            raise ValueError("Date format not recognized.")
        if i in self.__database:
            self.__database[i] = date
        else:
            raise KeyError("No such date index.")

    def queryDate(self, i):
        if i in self.__database:
            return f"The date is {self.__database[i]}"
        else:
            return "No such date found."

    def showAll(self):
        return self.__database