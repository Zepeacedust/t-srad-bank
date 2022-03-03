class Account:
    numberOfAccounts = 0
    
    def __init__(self, amount = 0):
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        #if given invalid value, use 0
        try:
            self.amount = float(amount)
        except ValueError:
            self.amount = 0
            
    
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
