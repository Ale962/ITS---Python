# Lesson 6 Exrcise 9.2

'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
'''

from Lesson_6_Exercise_9_1 import Restaurant

restaurant1 = Restaurant("Glande Asia", "Cinese")
restaurant2 = Restaurant("De Vikingr", "Nordic")
restaurant3 = Restaurant("Amikonos", "Grecks")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()