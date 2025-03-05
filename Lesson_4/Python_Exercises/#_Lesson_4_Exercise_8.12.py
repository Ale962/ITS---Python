# Lesson 4 Exercise 8.12

'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
'''

def sandwich_ingredients(list):
    while True:
        
        ingridient = input("What do you want in your sandwich?: ")

        list.append(ingridient)

        question = input("Do you want something more in the sandwich? (y/n): ")
        if question == "n":
            break
        else:
            continue

sandwich1: list = []
sandwich2: list = []
sandwich3: list = []

sandwich_ingredients(sandwich1)
sandwich_ingredients(sandwich2)
sandwich_ingredients(sandwich3)
