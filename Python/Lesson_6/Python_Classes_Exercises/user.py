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
    
class Privileges:
    
    def __init__(self, privilege: str = None):
        self.__privileges: list = []
        if privilege:
            self.add_privilege(privilege)

    def add_privilege(self, privilege):
        self.__privileges.append(privilege)

    def show_priviligies(self) -> list:
        print(self.__privileges)
        return self.__privileges
    
    def __str__(self) -> str:
        privilege_str = "The privileges are:"

        for pivilege in self.__privileges:
            privilege_str += "\n" + pivilege

        return privilege_str
    
class Admin:

    def __init__(self, admin: User, privilege: Privileges):
        self.set_admin(admin)
        self.set_prilege(privilege)

    def set_admin(self, admin: User):
        self.__admin = admin

    def set_prilege(self, privilege: Privileges):
        self.__privilege = privilege

    def get_admin(self):
        return self.__admin.describe_user()
    
    def get_privilege(self):
        return self.__privilege.show_priviligies()
    
    def __str__(self) -> str:

        str_admin: str = self.__admin.__str__() + "\n" + self.__privilege.__str__()

        return str_admin