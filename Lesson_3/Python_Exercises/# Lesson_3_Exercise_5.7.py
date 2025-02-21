# Lesson 3 Exercise 5.7

'''5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!'''

favorite_fruits: list[str] = ["Orange", "Apple", "Melon", "Cocconut", "Ananas"]

fruit: str = str(input("Write the fruit you want to eat here: "))

if fruit == favorite_fruits[0]:
    print(f"You really like {favorite_fruits[0]}")

elif fruit == favorite_fruits[1]:
    print(f"You really like {favorite_fruits[1]}")

elif fruit == favorite_fruits[2]:
    print(f"You really like {favorite_fruits[2]}")

elif fruit == favorite_fruits[3]:
    print(f"You really like {favorite_fruits[3]}")

elif fruit == favorite_fruits[4]:
    print(f"You really like {favorite_fruits[4]}")

else:
    print("Good choice!!")