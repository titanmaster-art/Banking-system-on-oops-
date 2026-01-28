# project 2
class BalanceException(Exception):
 pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. Balance = ${self.balance:.2f}")
        print(f"{self.balance}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount ):
        self.balance = self.balance + amount
        print(f"\nAccount'{self.name}' balance = ${self.balance:.2f}")
        print("\nDeposit complete.")

    def viableTransaction(self,amount):
        if  self.balance >= amount :
            return
        else:
            raise BalanceException(
              f"\n sorry,account'{self.name}' balance exceeds the balance of ${self.balance:.2f}.")
    def withdraw(self,amount ):

        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()

        except BalanceException as  error:
            print(f"withdraw interuupted:{error}")

    def transfer(self,amount,account):
        try:
            print('\n*******\n\n Beginning transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete.")

        except BalanceException as error:
            print(f"sorry your response is noted but pese nehi ha bhai")

class InterestRewardAcct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance+(amount*1.05)
        print("\ndeposit complete.")
        self.getBalance()

class SavingAcct(InterestRewardAcct):
    def __init__(self, initialAmount,acctName):
      super().__init__(initialAmount,acctName)
      self.fee = 5
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance = self.balance - (amount+self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"withdraw interuupted:{error}")

        def viableTransaction(self, amount):
            if self.balance >= amount:
                return
            else:
                raise BalanceException(
                    f"\n sorry,account'{self.name}' balance exceeds the balance of ${self.balance:.2f}.")




