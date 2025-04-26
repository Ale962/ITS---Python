# Lesson 3 Exercise 5.8

'''5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
'''

usernames: list[str] = ["admin", "Alessio", "Rachele", "Rebecca", "Riccardo", "Diego"]

user: str = str(input("Insert User name here: "))

if user == "admin":
    print(f"Hello admin, would you like to see a status report?")

else:
    print(f"Hello {user}, thank you for logging in again.")