# Lesson 3 Exercise 5.10

'''
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
'''

current_user: list[str] = ["Alessio", "Diego", "Rachele", "Rebecca", "Riccardo"]
new_users: list[str] = ["Diego", "Riccardo", "Claudio", "Domenico", "Luca"]

not_usable_names_1 = [ name.lower() for name in current_user ]
not_usable_names_2 = [ name.upper() for name in current_user ]

user: str = str(input("Put your user name here: "))

if user in current_user or new_users:
    print(f"Welcome back {user}, thank you for logging in today")

else:
    if user == new_users or not_usable_names_1 or not_usable_names_2:
        print("User name already taken, please restart the process and insert a new name")
    else:
        new_users.append(user)
        print(f"Hello {user}, thank you for joining us")