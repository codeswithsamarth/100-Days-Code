# static method is a define as method in class which does not require information from class

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self.balance += amount
            self.__log_transaction_method("deposit",250)
        else:
            print("Amount Should Be Greater Than Zero")

    def _is_valid_amount(self,amount):
        return amount > 0

    def __log_transaction_method(self,transaction_type,amount):
        print(f"Logging {transaction_type} of ${amount} New Balance:{self.balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <=  5

account = BankAccount("Samarth",500)
account.deposit(244)



