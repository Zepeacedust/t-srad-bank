class NegativeBalanceNotAllowed (Exception):
    pass

class IllegalWithdrawal (Exception):
    pass
class IllegalTransfer(Exception):
    pass

class Account:
    numberOfAccounts = 0
    accounts = []
    def __init__(self, amount = 0):
        float_amount = float(amount)
        if float_amount < 0:
            raise NegativeBalanceNotAllowed 
        self.amount = float_amount
        
        
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        Account.accounts.append(self)
    
    def withdraw(self, amount):
        remaining = self.amount - float(amount)
        if remaining < 0:
            raise IllegalWithdrawal
        self.amount = remaining
    
    def deposit(self, amount):
        self.amount += float(amount)
    
    def transfer(self, recipient, amount):
        float_amount = float(amount)
        if self.amount - float_amount < 0:
            raise IllegalTransfer
        self.amount -= float_amount
        recipient.amount += float_amount

    def __str__(self) -> str:
        return str(self.number).zfill(6)
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
        Account.accounts = []

    def total_balance():
        return sum([account.amount for account in Account.accounts])
