# Lesson 2 Exercise 3.1

'''3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.'''

names: list = ["Rebby", "Rachele", "Alessio", "Riccardo"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(*names, sep ="\n")