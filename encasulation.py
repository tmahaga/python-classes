class BankAccount:
    def __init__(self, balance, name ,acc_no):
        self.__balance=balance #Private attribute
        self._name=name #Protected attribute
        self.acc_no=acc_no #Public attribute
    def _deposit(self, amount):
        self.__balance += amount
        return f"New Balance: {self.__balance}"
    def get_balance(self):
        return self.__balance

account=BankAccount(1000, "John Doe", "12345")
print(account.get_balance())
#print(account.__balance)
print(account._deposit(500))  # This will raise an AttributeError because __deposit is private
print(account._name)
print(account.acc_no)