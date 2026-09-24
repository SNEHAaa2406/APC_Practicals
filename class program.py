class BankAccount:

    # Class variable
    account_counter = 1000

    # Constructor
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")

    # Display balance
    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    # Transfer money
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully")
        else:
            print("Insufficient balance for transfer")


# Creating two BankAccount objects
account1 = BankAccount("Sneha")
account2 = BankAccount("Rahul")


# Deposits
account1.deposit(5000)
account2.deposit(3000)

print()

# Display balances
account1.display_balance()
print()
account2.display_balance()

print()

# Withdrawal
account1.withdraw(1000)

# Transfer from account1 to account2
account1.transfer(2000, account2)

print()

# Final balances
account1.display_balance()
print()
account2.display_balance()