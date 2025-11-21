# Task 15 (Constructor + Classmethod + Staticmethod)
# Create a class Bank with:
# class attribute: bank_name
# instance attributes: name, balance
# methods: deposit(), withdraw(), profile()
# classmethod: change_bank_name()
# staticmethod: bank_policy() (print rules)
# Create multiple accounts and perform operations.


class Bank:

    bank_name = 'Bank of Baroda'

    def __init__(self, name, balance):
        self.acc_name = name
        self.curent_balance = balance
        
    def deposit(self):
        a = float(input("\nEnter amount to Deposit on your account: "))
        self.curent_balance += a
        print(f"Your diposit amount is {a}. \nAfter diposit account balance is: {self.curent_balance}.")

    def withdraw(self):
        b = float(input("\nEnter amount to withdraw on your account: "))
        if b > self.curent_balance:
            print("Enter safisante amount to withdraw.")
        else:
            self.curent_balance -= b
            print(f"You withdraw amount is {b}. \nAfter withdraw Account balance is: {self.curent_balance}.")

    def profile(self):
        print(f"\nBank Name      : {Bank.bank_name}")
        print(f"Account Holder : {self.acc_name}")
        print(f"Balance        : ₹{self.curent_balance}")

    @classmethod
    def change_bank_name(cls):
        new_bank_name = input("\nEnter new Bank name: ")
        cls.bank_name = new_bank_name
        print(f"Your Bank name is: {cls.bank_name}.")

    @staticmethod
    def bank_policy():
        print("\n--- BANK POLICY ---")
        print("1. Minimum balance must be ₹500.")
        print("2. ATM withdrawal limit: ₹25,000 per day.")
        print("3. Proper KYC documents are mandatory.")

b1 = Bank('Drashti', 20500.00)
b1.bank_policy()
b1.profile()
b1.withdraw()
b1.deposit()


b2 = Bank('Sejal', 2010)
b2.bank_policy()
b2.profile()
b2.withdraw()
b2.deposit()