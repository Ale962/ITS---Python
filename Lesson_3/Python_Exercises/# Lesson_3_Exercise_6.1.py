# Lesson 3 Exercise 6.1

'''
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
'''

person: dict = {"first_name": "Rachele", "last_name": "Corsi", "age": "26", "city": "Roma"}

print (person)
print (person["first_name"])
print (person["last_name"])
print (person["age"])
print (person["city"])

print (f"The person I know is {person['first_name']} {person['last_name']}, her age is {person['age']} and she lives in {person['city']}")