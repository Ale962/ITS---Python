class Account:

    def __init__(self, account_id: str, balance: float = 0):
        self.__set_account_id(account_id)
        self.__set_balance(balance)

    def __set_account_id(self, account_id: str)->None:
        self.__account_id = account_id

    def __set_balance(self, balance: float) -> None:
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float) -> None:
        self.__balance += amount

class Bank:

    def __init__(self, accounts: dict[str, Account] = None):
        if accounts:
            self.__accounts = accounts
        else:
            self.__accounts = {}

    def create_account(self, account_id: str) -> None:

        if account_id in self.__accounts:
            raise KeyError('Account with this ID already exists')

        else:
            new_account: Account = Account(account_id)
            self.__accounts[account_id] = new_account

    def deposit(self, account_id: str, amount: float) -> None:
        if account_id in self.__accounts:
            self.__accounts[account_id].deposit(amount)

    def get_balance(self, account_id:str) -> None:
        if account_id in self.__accounts:
            return self.__accounts[account_id].get_balance()
        else:
            raise KeyError('Account not found')