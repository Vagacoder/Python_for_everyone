## Ch09 R9.12

class BankAccount :

    def __init__(self, initialBalance = 0.0) :
        self._balance = initialBalance
        self._transactionTime = 5
        self._transactionFee = 1.0


    def deposit(self, amount) :
        self._balance = self._balance + amount
        if self._transactionTime >0:
            self._transactionTime -=1
        else:
            self._balance -= self._transactionFee


    def withdraw(self, amount) :
        
        if self._transactionTime >0:
            self._transactionTime -=1
        else:
            self._balance -= self._transactionFee
            
        PENALTY = 10.0
        if amount > self._balance :
            self._balance = self._balance - PENALTY
            self._transactionTime -=1
        else :         
            self._balance = self._balance - amount
            self._transactionTime -=1


    def addInterest(self, rate) :
        amount = self._balance * rate / 100.0
        self._balance = self._balance + amount
        self._transactionTime = 5


    def getBalance(self) :
        return self._balance
