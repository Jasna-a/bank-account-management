
class bank_account:
    def __init__(self,initial_balance):
        self.balance = initial_balance

    def deposit(self , amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} , Deposited Successfully")
        elif amount<=0:
            print("Enter an Amount greater than 0")
    def withdrawal(self,amount):
        if amount < 0:
            print("Enter an Amount greater than 0")
        elif amount <= self.balance:
            self.balance-= amount
            print("Amount withdrawal successfull")
        else :
            print("Insufficcient balance")
    def check_balance(self):
        print("Balance Amount = ",self.balance)
account2=bank_account(5000)
account2.deposit(5000)
account2.withdrawal(1500)
account2.check_balance()


