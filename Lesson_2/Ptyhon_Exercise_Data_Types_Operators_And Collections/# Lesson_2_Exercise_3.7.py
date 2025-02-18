# Lesson 2 Exercise 3.7

'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''

peopleIlike: list = ["Rebby", "Rachel", "Ricky", "Nonno Antonio"]
invite: str = "would you like to have a dinner with me?"

for people in peopleIlike:
    print(f"{people} {invite}")

invitecorrection1: str = "Nonno Antonio couldn't make it so:"
peopleIlike[3] = "Luca"

print(invitecorrection1)

for people in peopleIlike:
    print(f"{people} {invite}")

invitecorrection2: str = "I have found a bigger table, so there is room for more:"
peopleIlike.insert(0, "Arjol")
peopleIlike.insert(2, "Giada")
peopleIlike.append("Selvaggia")

print(invitecorrection2)

for people in peopleIlike:
    print(f"{people} {invite}")

invitecorrection3: str = "The Table I found was broken so I have room only for 2"
invdel1: str = "Apologies, I don't have room for you anymore, I'm sorry"

print(invitecorrection3)

while range(len(peopleIlike)>2):
    print(f"{invdel1} {peopleIlike[2]}")
    peopleIlike.pop(2)
    
for people in peopleIlike:
    print(f"{people} {invite}")

while range(len(peopleIlike)>0):
    del peopleIlike [0]
    
print(peopleIlike)