# print("sanity check")

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self


class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
        self.account.deposite(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


shay = User('Shalynn', 'snburger@gmail.com')

shay.make_deposit(200).make_withdraw(250).display_user_balance()



# shay = BankAccount(0.17, 500)

# maverick = BankAccount(0.25, 750)


# shay.deposite(90).deposite(45).deposite(350).withdraw(150).yield_interest().display_account_info()

# maverick.deposite(120).deposite(500).withdraw(10).withdraw(200).withdraw(70).withdraw(50).yield_interest().display_account_info()