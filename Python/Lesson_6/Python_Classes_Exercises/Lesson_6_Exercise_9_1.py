# Lesson 6 Exercise 9.1

'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

'''

class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def setRestaurantName(self, restaurant_name) -> None:
        self.restaurant_name = restaurant_name

    def setCuisineType(self, cuisine_type) -> None:
        self.cuisine_type = cuisine_type

    def getRestaurantName(self) -> str:
        return self.restaurant_name
    
    def getCuisineType(self) -> str:
        return self.cuisine_type
    
    def __str__(self) -> str:
        return f"The name of the restaurant is {self.restaurant_name} and the cousine typr is {self.cuisine_type}"
    
    def open_restaurant(self) -> None:
        print(f"The restaurant {self.restaurant_name} is open.")
        
    def describe_restaurant(self) -> None:
        print(f"The name of the restaurant is {self.restaurant_name} and the cousine typr is {self.cuisine_type}")

restaurant = Restaurant("Glande Asia", "Cinese")

restaurant.describe_restaurant()
restaurant.open_restaurant()