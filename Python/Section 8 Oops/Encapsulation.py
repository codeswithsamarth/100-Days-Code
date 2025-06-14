# Encapsulation is a ability to protect overrides of attributes

class BadBankAccount:
    def __init__(self,balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1

class Bank_Account:
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit Amount Must Be Positive")
        else:
            self.__balance += amount

    def withdraw(self,amount):
        if (amount<=0):
            raise ValueError("Deposit Amount Must Be Positive")
        if  amount >= self.__balance:
            raise ValueError("Insufficient Funds")
        else:
            self.__balance -= amount

account = Bank_Account(100)
print(account.balance)