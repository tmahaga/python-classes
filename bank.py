
#Mbaga Tuzinde mahaga 
#Admission no:BSCIT-01-0064/2025

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        # Initializing the attributes
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        # Adds the amount to the balance and returns the amount deposited
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        # Checks if there's enough balance before withdrawing
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        # Printing the current balance
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        # Printing all the customer's details
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Example
if __name__ == "__main__":
    # 1. Create a new account for testing
    my_account = BankAccount(
        account_number="ZET-123456", 
        balance=5000, 
        date_of_opening="2026-03-03", 
        customer_name="Mbaga Tuzinde"
    )

    # 2. Testing  the methods
    print("--- Customer Details ---")
    my_account.customer_details()
    
    print("\n--- Testing Transactions ---")
    deposited = my_account.deposit(1500)
    print(f"Amount Deposited: {deposited}")
    my_account.check_balance()
    
    withdrawn = my_account.withdraw(2000)
    print(f"Amount Withdrawn: {withdrawn}")
    my_account.check_balance()
    
    # Test insufficient funds
    failed_withdrawal = my_account.withdraw(10000)
    print(f"Attempting to withdraw 10000: {failed_withdrawal}")