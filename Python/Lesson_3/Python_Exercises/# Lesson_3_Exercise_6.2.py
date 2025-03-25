# Lesson 3 Exercise 6.2

'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
'''

numbers: dict = {"Rachele": 13, "Alessio": 22, "Rebecca": 3, "Diego": 17, "Riccardo": 7}

for key, value in numbers.items():
    print (key, value)