"""
Question 2: Functions + OOP 
Objective: Test Object-Oriented Programming concepts.
Problem Statement: Create a Bank Account System using classes.

Requirements=
Create a class BankAccount
Use init to initialize:
account_holder
balance

Create methods:
deposit(amount)
withdraw(amount)

Create a child class SavingsAccount that:
Inherits from BankAccount
Has interest_rate
Calculates yearly interest
"""

# ------------------------------------
# BankAccount -parent class
# ------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"{amount} Rs deposite successfully. New Balance: {self.balance} Rs.")
        else:
            print("Invalid Deposite amount.")
        

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} Rs withdraw successfully. Current Balance: {self.balance} Rs.")

    def display_acc_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}.")
        print(f"Balance: {self.balance} Rs.")
        print("-----------------------------")


# ------------------------------------
# SavingsAccount -child class
# ------------------------------------

class SavingsAccount(BankAccount):
    
    def __init__(self, account_holder, balance, interest_rate):
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate

    def calculates_yearly_interest(self):
        interest = (self.balance * self.interest_rate) / 100 
        print(f"Yearly Interest is {interest}.")
        return interest
    


# ------------------------------------
# create SavingsAccount object
# ------------------------------------

account = SavingsAccount("Drashti", 20000, 5)

account.display_acc_details()
account.deposit(3000)
account.withdraw(500)
account.calculates_yearly_interest()
