# Lesson 6 Exercise 9.3

'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

'''

class User:
    def __init__(self, first_name: str, last_name: str, email: str, telephone: int):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_telephone(telephone)

    def set_first_name(self, first_name: str) -> str:
        
        if first_name == "":
            print("error: must not have an empty field")
        else:
            self.first_name = first_name
    
    def set_last_name(self, last_name: str) -> str:

        if last_name == "":
            print("error: must not have an empty field")
        else:
            self.last_name = last_name
    
    def set_email(self, email: str) -> str:

        if email == "":
            print("error: must not have an empty field")
        else:
            self.email = email
    
    def set_telephone(self, telephone: int) -> int:

        if telephone == None:
            print("error: must not have an empty field")
        else:
            self.telephone = telephone

    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_email(self) -> str:
        return self.email
    
    def get_telephone(self) -> int:
        return self.telephone
    
    def describe_user(self) -> None:
        print(f"User name: {self.first_name}\nUser last name: {self.last_name}\nUser email: {self.email}\nUser telephone: {self.telephone}")
    
    def greet_user(self) -> None:
        print(f"Hello {self.first_name} {self.last_name}! It's nice to see you logging in today!")
    
user1 = User("Alessio", "Caico", "alec@blah.com", 26121351313581)

user1.greet_user()
user1.describe_user()

user2 = User("Rachele", "Corsi", "racc@blah.com", 26121351313582)

user2.greet_user()
user2.describe_user()

user3 = User("Davive", "Mugno", "davm@blah.com", 26121351313583)

user3.greet_user()
user3.describe_user()