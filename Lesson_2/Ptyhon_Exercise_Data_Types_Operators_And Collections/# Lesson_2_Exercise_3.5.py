# Lesson 2 Exercise 3.5

'''3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

peopleIlike: list = ["Rebby", "Rachel", "Ricky", "Nonno Antonio"]
invite: str = "would you like to have a dinner with me?"

for people in peopleIlike:
    print(f"{people} {invite}")

invitecorrection1: str = "Nonno Antonio couldn't make it so:"
peopleIlike[3] = "Luca"

print(invitecorrection1)

for people in peopleIlike:
    print(f"{people} {invite}")