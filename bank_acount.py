#%%
class bankaccount():
    defaultbankaccnumber = 1
    
    def __init__(self , name , balance = 0):
        self.name = name
        self.balance = balance
        self.accountnumber = bankaccount.defaultbankaccnumber
        bankaccount.defaultbankaccnumber = bankaccount.defaultbankaccnumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient balance")
        else:
            self.balance -= amount

    def getbalance(self):
        return self.balance
# %%
myacc = bankaccount("omkar", 20000)
myacc.deposit(1000)
print(myacc.getbalance())
# %%
