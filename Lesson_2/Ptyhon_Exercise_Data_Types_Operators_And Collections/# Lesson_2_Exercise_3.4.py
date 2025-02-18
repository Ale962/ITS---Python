# Lesson 2 Exercise 3.4

'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.'''

peopleIlike: list = ["Rebby", "Rachel", "Ricky", "Nonno Antonio"]
invite: str = "would you like to have a dinner with me?"

for people in peopleIlike:
    print(f"{people} {invite}")