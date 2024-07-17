class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest ${interest}. New balance is ${self.balance}.")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")

# Test the banking system

# Create a Savings Account
savings = SavingsAccount(account_number="SA123", account_holder="Alice", balance=1000, interest_rate=0.05)
savings.deposit(200)
savings.withdraw(150)
savings.add_interest()
print(f"Savings Account Balance: ${savings.get_balance()}")

# Create a Checking Account
checking = CheckingAccount(account_number="CA456", account_holder="Bob", balance=500, overdraft_limit=100)
checking.deposit(300)
checking.withdraw(700)
checking.withdraw(200)  # This should fail due to overdraft limit
print(f"Checking Account Balance: ${checking.get_balance()}")
