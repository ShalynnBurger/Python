# print("sanity check")

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        # if self.balance<0:
        # self.balance -= 5
        # print("Insufficient funds: Charging a $5 fee")

        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        (self.balance*self.int_rate) + self.balance
        print(self.yield_interest)
        return self

class User