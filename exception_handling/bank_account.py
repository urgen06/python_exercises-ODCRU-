class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        return self.balance
    
    def withdrawal(self, amount):
        if self.balance < amount:
            raise InsufficientBalanceError(f"No Sufficeint Balance. You have {self.balance} and you are tyring to withdraw {amount}")
        else:
          self.balance -=  amount
          return self.balance

account = BankAccount(500)

while True:
    operation = input("You want to deposit/ withdraw/ quit? ")
    
    if operation.lower() == 'quit':
        print("Have a nice day!")
        exit()

    amount = float(input("Amount you want to deposit/withdraw: "))

    if operation.lower() == "deposit":
        total = account.deposit(amount) 
        print(f"Total balance after deposit: {total}")
    
    if operation.lower() == "withdraw":
        try:
            total = account.withdrawal(amount)
            print(f"Total balance after withdrawal : {total}")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")
    
    



