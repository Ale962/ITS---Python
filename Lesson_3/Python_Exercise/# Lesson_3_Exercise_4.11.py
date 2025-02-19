# Lesson 3 Exercise 4.11

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'''

pizzas: list = ["Margherita", "4 Formaggi", "Boscaiola", "Diavola"]
friend_pizzas: list = ["Margherita", "4 Formaggi", "Boscaiola", "Diavola"]

pizzas.append("Marinara")
friend_pizzas.append("Capricciosa")

print("My favorite pizzas are:")
for items in pizzas:
    print(items)

print("My friend favorite pizzas are:")
for items in friend_pizzas:
    print(items)