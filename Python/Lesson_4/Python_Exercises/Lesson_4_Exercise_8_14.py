# Lesson 4 Exercise 8.14

'''
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 

'''

def car_information(manufacturer: str, model: str, year: int, color: str) -> dict:

    car_info_dict: dict = {}

    car_info_dict["manufcturer"] = manufacturer
    car_info_dict["model"] = model
    car_info_dict["year"] = year
    car_info_dict["color"] = color

    return car_info_dict

print(car_information("Alfa Romeo", "Stelvio", 2020, "Bordo"))