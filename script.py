
from bank_accounts import *

class BankAccount:
 Dave = BankAccount(1000, "Dave")
 sara = BankAccount(1000, "sara")
 Dave.deposit(100)

 sara.withdraw(1400)
 Dave.transfer(100000,sara)

 jim = InterestRewardAcct(1000,"jim")

 jim.getBalance()

 jim.transfer(1200,Dave)
 jim.withdraw(100)

 strong = SavingAcct(100,"strong")

 strong.getBalance()
 strong.withdraw(90)
 strong.viableTransaction(10000,Dave)
