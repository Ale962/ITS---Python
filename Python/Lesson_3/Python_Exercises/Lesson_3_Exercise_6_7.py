# Lesson 3 Exercise 6.7

'''
6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
'''

person2: dict = {"first_name": "Rebby", "last_name": "De Rosa", "age": "25", "city": "Rome"}
person3: dict = {"first_name": "Riccardo", "last_name": "Paladini", "age": "20", "city": "Rome"}
person4: dict = {"first_name": "Samuele", "last_name": "Vona", "age": "23", "city": "Ariccia"}

people = [person2, person3, person4]


for p in people:
    
    for value in p.values():
        print(value)