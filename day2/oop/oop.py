 class BankAccount(object):

    def _init_(self):
        pass

    def withdraw():
        pass
    def deposit():
        pass

class SavingsAccount(BankAccount):

    def _init_(self):
        self.balance = 500

    def deposit(self, cashDeposit):
        if (cashDeposit < 0):
            return "Invalid deposit amount"
        else:
            self.balance += cashDeposit
            return self.balance
            
    def withdraw(self, cashWithdraw):
        if ((self.balance - cashWithdraw) > 0) and ((self.balance - cashWithdraw) < 500):
            return "Cannot withdraw beyond the minimum account balance"
        elif (self.balance - cashWithdraw) < 0:
            return "Cannot withdraw beyond the current account balance"
        elif cashWithdraw < 0:
            return "Invalid withdraw amount"
        else:
            self.balance -= cashWithdraw
            return self.balance 

class CurrentAccount(BankAccount):

    def _init_(self):
        self.balance = 0

    def deposit(self, cashDeposit):
        if cashDeposit < 0:
            return "Invalid deposit amount"
        else:
            self.balance += cashDeposit
            return self.balance

    def withdraw(self, cashDeposit):
        if cashDeposit < 0:
            return "Invalid withdraw amount"
        elif self.balance < cashDeposit:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= cashDeposit
            return self.balance