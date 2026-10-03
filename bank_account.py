# this is a simple bank account where customers can have multiple accounts and make transactions.

class Transaction():
  def __init__(self,amount,date,owner,transaction_type):
    self.owner=owner
    self.amount=amount
    self.date=date
    self.transaction_type=transaction_type
    

class BankAccount();
  def __init__(self,account_number,account_type,hidden_bal):
    self.account_number=account_number
    self.account_type=account_type
    self.hidden_bal=hidden_bal

    def savings(self,account_number,account_type):

    def current(self,account_number,account_type):

class Customer():
  def __init__(self,name,cusid):
    self.name=name
    self.cusid=cusid


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
savings.withdraw(99999)   # should raise error or print message

# Print statement
savings.get_statement()

# Print customer summary
print(alice)
print("Total balance:", alice.total_balance())

# Apply interest to savings
savings.apply_interest()
print("After interest:", savings.balance)