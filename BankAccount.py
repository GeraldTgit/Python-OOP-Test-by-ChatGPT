"""Define a class called BankAccount that has the following attributes and methods:
Attributes:
balance (float): the balance of the account
interest_rate (float): the interest rate on the account"""
class BankAccount:
    def __init__(self, balance: float, interest_rate: float):
        self.balance = balance
        self.interest_rate = interest_rate
        
#Methods:
    #deposit(amount: float): adds amount to the balance
    def deposit(self, amount: float):
        self.balance = self.balance + amount
        return self.balance

    #withdraw(amount: float): removes amount from the balance
    def withdraw(self, amount: float):
        self.balance = self.balance - amount
        return self.balance

    #add_interest(): adds the interest earned based on the interest_rate to the balance
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest
        return self.balance

    #get_balance() -> float: returns the current balance of the account
    def get_balance(self):
        return self.balance

    #get_interest_rate() -> float: returns the current interest rate on the account
    def get_interest_rate(self):
        return self.interest_rate

"""Define a subclass called SavingsAccount that inherits from the BankAccount class and has an additional attribute:
Attributes:
min_balance (float): the minimum balance required in the account"""
class SavingsAccount(BankAccount):
    def __init__(self, balance: float, interest_rate: float, min_balance: float):
        super().__init__(balance, interest_rate)
        self.min_balance = min_balance

#Methods:
    #withdraw(amount: float): removes amount from the balance only if the resulting balance is greater than or equal to the min_balance
    def withdraw(self, amount: float):
        if amount >= self.min_balance:
            self.balance = self.balance - amount
            return self.balance

    # add_interest(): adds the interest earned based on the interest_rate to the balance only if the current balance is greater than or equal to the min_balace
    def add_interest(self):
        if self.balance >= self.min_balance:
            interest = self.balance * self.interest_rate
            self.balance = self.balance + interest
            return self.balance

"""Define a subclass called CheckingAccount that inherits from the BankAccount class and has an additional attribute:
Attributes:
transaction_fee (float): the fee charged for each transaction (deposit or withdrawal)"""
class CheckingAccount(BankAccount):
    def __init__(self, balance: float, interest_rate: float, trasaction_fee: float):
        super().__init__(balance, interest_rate)
        self.trasaction_fee = trasaction_fee

#Methods:
    #deposit(amount: float): adds amount to the balance but subtracts the transaction_fee
    def deposit(self, amount: float):
        self.balance = self.balance + amount - self.trasaction_fee
        return self.balance 

    #withdraw(amount: float): removes amount from the balance but subtracts the transaction_fee
    def withdraw(self, amount: float):
        self.balance = self.balance - amount - self.trasaction_fee
        return self.balance

    #deduct_fees(num_transactions: int): subtracts num_transactions * transaction_fee from the balance
    def deduct_fees(self, num_transactions: int):
        fees = num_transactions * self.trasaction_fee
        self.balance = self.balance - fees
        return self.balance

#Create an instance of SavingsAccount and an instance of CheckingAccount. Test all of the methods on each instance to make sure they return the expected output.

account1 = BankAccount(29.26,0.3)
account2 = SavingsAccount(29.26,0.3,5.5)
account3 = CheckingAccount(29.26,0.3,1.12)

print(account1.deposit(5.1))
print(account1.withdraw(3))
print(account1.add_interest())
print(account1.get_balance())
print(account1.get_interest_rate())

print(account2.withdraw(5.6))
print(account2.add_interest())

print(account3.deposit(10))
print(account3.withdraw(9.9))
print(account3.deduct_fees(2))
