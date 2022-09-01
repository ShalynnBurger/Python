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


shay = BankAccount(0.17, 500)

maverick = BankAccount(0.25, 750)

shay.deposite(90).deposite(45).deposite(350).withdraw(150).yield_interest().display_account_info()

maverick.deposite(120).deposite(500).withdraw(10).withdraw(200).withdraw(70).withdraw(50).yield_interest().display_account_info()