# Lesson 3 Exercise 9.4 

'''
9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
'''


class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):

        self.set_restaurant_name(restaurant_name)
        self.set_cuisine_type(cuisine_type)
        self.set_number_served(number_served)

    def set_restaurant_name(self, restaurant_name) -> None:
        self.__restaurant_name = restaurant_name

    def set_cuisine_type(self, cuisine_type) -> None:
        self.__cuisine_type = cuisine_type

    def set_number_served(self, number_served) -> None:
        self.__number_served = number_served

    def get_restaurant_name(self) -> str:
        return self.__restaurant_name
    
    def get_cuisine_type(self) -> str:
        return self.__cuisine_type
    
    def get_number_served(self) -> int:
        return self.__number_served
    
    def __str__(self) -> str:
        return f"The name of the restaurant is {self.get_restaurant_name()} and the cousine type is {self.get_cuisine_type()}, today they have served {self.get_number_served()} customers"
    
    def open_restaurant(self) -> None:
        print(f"The restaurant {self.get_restaurant_name()} is open.")
        
    def describe_restaurant(self) -> None:
        print(f"The name of the restaurant is {self.get_restaurant_name()} and the cousine typr is {self.get_cuisine_type()}")

    def increment_number_served(self, number: int):
        self.__number_served += number
        return self.__number_served
    
restaurant = Restaurant("Glande Asia", "Cinese")

print(restaurant.get_number_served())

restaurant = Restaurant("Glande Asia", "Cinese", 5)

print(restaurant.get_number_served())
print(restaurant.set_number_served(10))
print(restaurant.get_number_served())
print(restaurant.increment_number_served(52))
print(restaurant.get_number_served())