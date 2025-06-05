# Optional Exercise 8

'''
8. ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
     Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.

'''
import random

accounts: list[dict[str, str|float]] = []


def InitializeAccount(name: str, surname: str, balance: float = 0.0) -> dict:
    pool1: list = list(l for l in name)
    pool2: list = list(ls for ls in surname)
    pool3: list = list(str(n) for n in range(0, 10))
    unique_code_list = random.sample(pool1, 3) + random.sample(pool2, 3) + random.sample(pool3, 4)
    random.shuffle(unique_code_list)
    unique_code_str = "".join(unique_code_list)
    return{"name": name,"surname": surname, "balance": balance, "unique_code": unique_code_str}

def ATM() -> list[dict[str, str|float]]:
    while True:
        question = input(
            "Select operation:\n" \
            "A to add account\n" \
            "D to deposit\n" \
            "W to withdraw\n" \
            "C to check balance of the given account\n" \
            "Q to quit the process\n" \
            "Select option: ")
        print("--------------------")
        match question.upper():
            case "A":
                name = input("Insert your name here: ")
                surname = input("Insert your surname here: ")
                balance = float(input("Insert the starting balance here: "))
                print("--------------------")
                while True:
                    new_account = InitializeAccount(name, surname, balance)
                    if all(a.get("unique_code") != new_account["unique_code"] for a in accounts):
                        accounts.append(new_account)
                        print(f"New account created")
                        print(f"Account name: {name}")
                        print(f"Account surname: {surname}")
                        print(f"Account balance: {balance}")
                        print(f"Unique code of the account: {new_account['unique_code']}")
                        print("--------------------")
                        break           
            case "D":
                name = input("Insert your name here: ")
                unique_code = input("Insert the account unique code here: ")
                balance = float(input("Insert the amount to deposit: "))
                print("--------------------")
                Deposit(name, unique_code, balance)
                print("--------------------")
            case "W":
                name = input("Insert your name here: ")
                unique_code = input("Insert the account unique code here: ")
                balance = float(input("Insert the amount to withdraw: "))
                print("--------------------")
                Withdraw(name, unique_code, balance)
                print("--------------------")
            case "C":
                name = input("Insert your name here: ")
                unique_code = input("Insert the account unique code here: ")
                print("--------------------")
                CheckAccount(name, unique_code)
                print("--------------------")
            case "Q":
                print("Thank you for using our ATM simulator!")
                print("Have a good day!")
                print("--------------------")
                break
            case _:
                print("Invalid option selected, please select a valid option.")
                print("--------------------")

def Deposit(name: str, unique_code: str, balance: float, accounts: list[dict[str, str|float]] = accounts):
    found: bool = False
    for a in accounts:
        if a.get("name") == name and a.get("unique_code") == unique_code:
            found = True
            a["balance"] += balance
            print(f"Account found, name: {a['name']}, unique code: {a['unique_code']}, balance modified: {a['balance']}")
    if found == False:
        print("Account not found")

def Withdraw(name: str, unique_code: str, balance: float, accounts: list[dict[str, str|float]] = accounts):
    found: bool = False
    for a in accounts:
        if a.get("name") == name and a.get("unique_code") == unique_code:
            found = True
            if a.get("balance") > balance:
                a["balance"] -= balance
                print(f"Account found, name: {a['name']}, unique code: {a['unique_code']}, balance modified: {a['balance']}")
            else:
                print("Available funds not enough to withdraw the desired amount. Please restart operation")
    if found == False:
        print("Account not found")

def CheckAccount(name: str, unique_code: str, accounts: list[dict[str, str|float]] = accounts):
    found: bool = False
    for a in accounts:
        if a.get("name") == name and a.get("unique_code") == unique_code:
            found = True
            print(f"Account found, name: {a['name']}, surname: {a['surname']}, unique code: {a['unique_code']}, balance: {a['balance']}")
    if found == False:
        print("Account not found")


if __name__ == "__main__":
    ATM()