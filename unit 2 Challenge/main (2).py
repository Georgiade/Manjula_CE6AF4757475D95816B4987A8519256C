class  BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print("Deposited ${}, new balance is ${}".format(amount,self.account_balance))
         
        else:
         print("Invalid deposit amount.")
         
    def withdraw(self,amount):
        if amount > 0 and amount <= self.account_balance:
         self.account_balance -= amount
         print("withdraw ${}, New balance: ${}".format(amount,self.account_balance))
         
        else:
         print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
     print("Account balance for {} (Amount {}): ${}".format(
      self.account_holder_name, self.account_number,
      self.account_balance))

#create an withdraw of the bank account class
account = BankAccount(account_number="123456789",
                     account_holder_name="manjula",
                     initial_balance=5000.0)
#Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
