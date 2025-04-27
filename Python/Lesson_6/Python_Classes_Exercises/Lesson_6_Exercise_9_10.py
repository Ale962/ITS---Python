# Lesson 6 Exercise 9.10

'''
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

'''

from Lesson_6_Exercise_9_4 import Restaurant

restaurant = Restaurant("Glande Asia", "Cinese")

print(restaurant)

restaurant.increment_number_served(100)

print(restaurant)

restaurant.increment_number_served(20)

print(restaurant)

restaurant.increment_number_served(-10)

print(restaurant)