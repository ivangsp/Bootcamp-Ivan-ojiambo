class BankAccount(object):

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance+=amount 
            return self.balance   

    # def withdraw(self, amount):
    #     if amount < 0:
    #         raise ValueError('Insufficient balance on account')

    #     self.balance-=amount
    #     if self.balance <0:
    #        return "insufficient balance" 

    #     else:
    #         return self.balance
 
class SavingsAccount(BankAccount):

    def __init__(self):
        self.balance = 5000
            
    def withdraw(self, amount):
        #self.balance = BankAccount.withdraw(amount)
        self.balance-=amount
        if self.balance < 500:
            return "Cannot withdraw beyond the minimum account balance"
        else:
            return self.balance

class CurrentAccount(BankAccount):

    def __init__(self):
        self.balance = 10000

    def withdraw(self, amount):
        
        #self.balance = BankAccount.withdraw(amount)
        self.balance -=amount
        if self.balance < 10000:
            return "Cannot withdraw beyond the min balance"
        else:
            return self.balance

saving_account  = SavingsAccount()
current_account = CurrentAccount()

print saving_account.deposit(20000)
print saving_account.withdraw(30000)

print current_account.deposit(10000)
print current_account.withdraw(15000)

        