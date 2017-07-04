class BankAccount(object):

    def __init__(self, account, person_name):
      self.account_number == account
      self.person_name  = person_name
      self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance+=amount 
            return('{} you have successfully deposited {} and you account balance is {}'.format(self.person_name, amount, self.balance))
 
class SavingsAccount(BankAccount):

    def __init__(self, account, name):
        super(BankAccount, self).__init__()
        self.balance = 5000
        self.max_withdraw =2000000
        self.person_name = name

            
    def withdraw(self, amount):
        if amount <0:
            return('Invalid amount')
        elif amount > self.max_withdraw:
            return('On saving_account u can not withdraw more than 2m')
        else:
            self.balance-=amount
            if self.balance < 5000:
                return("{} you Cannot withdraw beyond the minimum account balance".format(self.person_name))
            else:
                return ('{} you have successfully withdrew {} \n your account balance is {}'.format(self.person_name, amount, self.balance))

class CurrentAccount(BankAccount):

    def __init__(self, account, name):
        super(BankAccount, self).__init__()
        self.balance = 10000
        self.max_withdraw = 10000000
        self.person_name = name

    def withdraw(self, amount):
        
        if amount <0:
            return('Invalid amount')
        elif amount > self.max_withdraw:
            return('On current account u can not withdraw more than 10m')
        else:
            self.balance-=amount
            if self.balance < 10000:
                return("{} you Cannot withdraw beyond the minimum account balance".format(self.person_name))
            else:
                return ('{} you have successfully withdrew {} \n your account balance is {}'.format(self.person_name, amount, self.balance))

saving_account  = SavingsAccount('0123444', 'gsp ivan')
current_account = CurrentAccount('018900', ' clement john')

print(saving_account.deposit(3000000)+"\n")
print(saving_account.withdraw(21000000)+"\n")

print(current_account.deposit(10000))
print(current_account.withdraw(15000))

        