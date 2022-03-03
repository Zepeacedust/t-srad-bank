class NegativeBalanceNotAllowed (Exception):
    pass

class Account:
    numberOfAccounts = 0
    
    def __init__(self, amount = 0):
        float_amount = float(amount)
        if float_amount < 0:
            raise NegativeBalanceNotAllowed 
        self.amount = float_amount
        
        
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
    
    def withdraw(self, amount):
        self.amount -= float(amount)
    
    def deposit(self, amount):
        self.amount += float(amount)
    
    def transfer(self, recipient, amount):
        float_amount = float(amount)
        self.amount -= float_amount
        recipient.amount += float_amount

    def __str__(self) -> str:
        return str(self.number).zfill(6)
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
