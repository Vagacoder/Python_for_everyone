## class portfolio for Ch09 P9.22

from bankaccount import BankAccount

class Portfolio:
    
    def __init__(self):
        
        self._checking = BankAccount()
        self._saving = BankAccount()
        
    def withdraw(self, amount, account):
        if account.upper() == 'C':
            self._checking.withdraw(amount)
        else:
            self._saving.withdraw(amount)
    
    def deposit(self, amount, account):
        if account.upper() == 'C':
            self._checking.deposit(amount)
        else:
            self._saving.deposit(amount)

    
    def transfer(self, amount, account):
        if account.upper() == 'C':
            self._checking.withdraw(amount)
            self._saving.deposit(amount)
        else:
            self._saving.withdraw(amount)
            self._checking.deposit(amount)

    
    def getBalance(self, account):
        if account.upper() == 'C':
            return self._checking.getBalance()
        else:
            return self._saving.getBalance()
    