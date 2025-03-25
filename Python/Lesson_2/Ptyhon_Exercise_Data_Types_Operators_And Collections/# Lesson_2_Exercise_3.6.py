# Lesson 2 Exercise 3.6

'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

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