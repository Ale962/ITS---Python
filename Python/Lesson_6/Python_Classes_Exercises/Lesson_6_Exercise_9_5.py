# Lesson 6 Exercise 9.5

'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

'''

class User:
    def __init__(self, first_name: str, last_name: str, email: str, telephone: int, login_attempts: int= 0):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_telephone(telephone)
        self.__login_attempts = login_attempts

    def set_first_name(self, first_name: str) -> str:
        
        if first_name == "":
            print("error: must not have an empty field")
        else:
            self.__first_name = first_name
    
    def set_last_name(self, last_name: str) -> str:

        if last_name == "":
            print("error: must not have an empty field")
        else:
            self.__last_name = last_name
    
    def set_email(self, email: str) -> str:

        if email == "":
            print("error: must not have an empty field")
        else:
            self.__email = email
    
    def set_telephone(self, telephone: int) -> int:

        if telephone == None:
            print("error: must not have an empty field")
        else:
            self.__telephone = telephone

    def get_login_attempts(self) -> int:
        return self.__login_attempts

    def get_first_name(self) -> str:
        return self.__first_name
    
    def get_last_name(self) -> str:
        return self.__last_name
    
    def get_email(self) -> str:
        return self.__email
    
    def get_telephone(self) -> int:
        return self.__telephone
    
    def increment_login_attempts(self, number: int = 1) -> None:
        self.__login_attempts += number
        

    def reset_login_attempts(self) -> None:
        self.__login_attempts = 0
    
    def describe_user(self) -> None:
        print(f"User name: {self.get_first_name()}\nUser last name: {self.get_last_name()}\nUser email: {self.get_email()}\nUser telephone: {self.get_telephone()}")
    
    def greet_user(self) -> None:
        print(f"Hello {self.get_first_name()} {self.get_last_name()}! It's nice to see you logging in today!")

    def __str__(self) -> str:
        return f"Hello {self.get_first_name()} {self.get_last_name()}, you have login today {self.get_login_attempts()} times, welcome back!"
    

user1 = User("Alessio", "Caico", "alec@blah.com", 26121351313581)

print(user1)

user1.increment_login_attempts()

print(user1)

user1.increment_login_attempts()

print(user1)

user1.increment_login_attempts()

print(user1)

user1.increment_login_attempts()

print(user1)

user1.reset_login_attempts()

print(user1)