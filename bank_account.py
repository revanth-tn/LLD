# this is a simple bank account where customers can have multiple accounts and make transactions.
from datetime import datetime 

class Transaction():
  def __init__(self,amount,date,owner,transaction_type):
    self.owner=owner
    self.amount=amount
    self.date=date
    self.transaction_type=transaction_type
    
  def __str__(self):
    return f"{self.amount} {self.date} {self.owner}"
    

class BankAccount():
  interest=0.05
  def __init__(self,account_number,account_type,balance):
    self.account_number=account_number
    self.account_type=account_type
    self.__balance=balance
    self.transactions=[]
    
  @property
  def balance(self):
    return self.__balance

    
  def deposit(self,amount):
    if(amount<=0):
      raise ValueError("amount depositing cannot be 0 or less than 0")
    else:
      self.__balance+=amount
      date = datetime.now()
      owner = self.account_number
      transaction_type = "deposit"

      store=Transaction(amount,date,owner,transaction_type)
      self.transactions.append(store)

  def withdraw(self,amount):
    if amount>self.__balance or amount<=0:
      raise ValueError("invalid")
    else:
      self.__balance-=amount
      date = datetime.now()
      owner = self.account_number
      transaction_type = "withdrawal"

      store=Transaction(amount,date,owner,transaction_type)
      self.transactions.append(store)

  def apply_interest(self):
    self.__balance=self.__balance+(self.__balance*self.interest)

  def get_statement(self):
    for transaction in self.transactions:
      print(transaction)

 
    

class Customer():
  def __init__(self,name,cusid):
    self.name=name
    self.cusid=cusid
    self.accounts=[]

  def add_account(self,account):
    self.accounts.append(account)

  def get_account(self,account_number):
    for account in self.accounts:
      if account.account_number == account_number:
        return account
      
  def total_balance(self):
    total=0
    for account in self.accounts:
      total+=account.balance
    return total

  def __str__(self):
    return f"{self.name} {self.cusid}"
    
if __name__ == "__main__":

# Create customer
  alice = Customer("Alice", "C001")

# Create accounts
  savings = BankAccount("A001", "savings", 1000)
  current = BankAccount("A002", "current", 500)

# Add accounts to customer
  alice.add_account(savings)
  alice.add_account(current)

# Do transactions
  savings.deposit(200)
  savings.withdraw(100)
  current.deposit(1000)

# Try invalid transaction
  #savings.withdraw(99999)   # should raise error or print message

# Print statement
  savings.get_statement()

# Print customer summary
  print(alice)
  print("Total balance:", alice.total_balance())

# Apply interest to savings
  savings.apply_interest()
  print("After interest:", savings.balance)
