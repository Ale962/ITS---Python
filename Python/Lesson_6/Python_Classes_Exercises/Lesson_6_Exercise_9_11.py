# Lesson 6 Exercise 9.11


'''
9-11. Imported Admin: Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.

'''

from user import *

user1 = User("Alessio", "Caico", "alec@blah.com", 1234567890)

privileges1 = Privileges("can add post")
privileges1.add_privilege("can delete post")

admin1 = Admin(user1, privileges1)

print(admin1)
print("\n")
admin1.get_admin()
print("\n")
admin1.get_privilege()
