# Lesson 4 Exercise 8.6

'''
 Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
'''

def city_country(city: str, country: str):
    print(f"{city}, {country}")

i = 1

while i <= 3:
    
    city: str = input("Write the name of the city here: ")
    country: str = input("Write the country of the city here: ")

    city_country(city, country)

    i += 1