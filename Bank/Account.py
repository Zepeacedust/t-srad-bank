class Account:
    numberOfAccounts = 0
    
    def __init__(self, amount = 0):
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        self.amount = float(amount)    
    
    def withdraw(self, amount):
        self.amount -= float(amount)
    
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
