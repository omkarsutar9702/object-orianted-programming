#%%
#special methods
# __init__ is a Magic method. Also __str__, __repr__, __add__ are all magic methods.
class Employee():
    def __init__(self, firstname,lastname, salary=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        
    def __str__(self):
        return "Full Name: " + self.firstname + " " + self.lastname

    def __int__(self):
        return self.salary
    
    def __eq__(self, other):
        return self.salary == other.salary
        
    def __add__(self, other):
        return self.salary + other.salary
    
    def __sub__(self, other):
        return self.salary - other.salary
    
    def __mul__(self, other):
        return self.salary * other.salary  
# %%
omkar = Employee("Omkar", "sutar" , 25000)
vrunda = Employee("Vrunda", "patil", 30000)

# %%
print(omkar)
print(vrunda) #(This output because of __str__ method overloading)
print(omkar + vrunda) # (This output because of __add__ method overloading)
print(omkar * vrunda) # (This output because of __mul__ method overloading)
print(omkar == vrunda) # (This output because of __eq__ method overloading)
print(int(omkar))
# %%
## proparty decorator 
## without proparty decorator
class bank_balance:
    def __init__(self , name , balance = 0):
        self.name = name
        self.balance = balance
        self.total = self.name + " has " + self.balance
    
user1 = bank_balance("user1", "10000")
user1.name = 'omkar'
print(user1.total)
print(user1.name)
# %%
class bank_balance:
    def __init__(self , name , balance = 0):
        self.name = name
        self.balance = balance
    @property        
    def total(self):
        return self.name + " has " +       self.balance
    
user1 = bank_balance("user1", "10000")
user1.name = 'omkar'
print(user1.total)
print(user1.name)
# %%
