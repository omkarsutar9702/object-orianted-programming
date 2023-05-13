################################## how to define a class ################################
#class name myClass
class myClass():
    # class attribute
    var = 30

#### creating first object or instance ####
firstObject = myClass()
print(firstObject) # prints myClass object memory address
### accessing class attribute ###
print(firstObject.var) # prints 30

### creating second object or instance ####
secondObject = myClass()
print(secondObject) # prints myClass object memory address
### accessing class attribute ###
print(secondObject.var)

### instance method ###
class vehicle():
    ## instance method
    def type(self):
        print(self)
        print("i have type method")

car = vehicle()
print(car)
car.type()

#### constructor method ###

class vehicle2():
    def __init__(self):
        print("calling constructor __init__")
        self.val = 0
        self.cost = 10000  ## setting default value when object is created

    def increamentcost(self):
        self.cost += 2000 ### increment cost by 2000

car2 = vehicle2() # init method is called
print("first cars cost", car2.cost)

car2.increamentcost() ## calling instance method increment cost
print("first objest after increament cost", car2.cost)

bike = vehicle2()
print("bike cost", bike.cost)

#### fisrt oop program ####

class maxsizelist():
    def __init__(self, value):
        self.value = value
        self.mylist = []
        
    def push(self , string):
        try:
            string = str(string)
            self.mylist.append(string)
        except ValueError:
            print("you can only push strings")

    def getlist(self):
        print(self.mylist[-self.value:])

if __name__ == "__main__":
    a = maxsizelist(2)
    b = maxsizelist(1)
    
    a.push('Hey')
    a.push('Hello')
    a.push('Hi')
    a.push('Let\'s')
    a.push('Go')
    
    b.push('Hey')
    b.push('Hello')
    b.push('Hi')
    b.push('Let\'s')
    b.push('Go')
    
    a.getlist()
    b.getlist()
    
### inharitance ###
class data ():
    def getdata(self):
        print("im data")
        
class time(data):
    def gettime(self):
        print("im time")
        
class space(time):
    def getspace(self):
        print("i am space")

if __name__ == "__main__":
    Data = data()
    Time = time()
    Space = space()

    Data.getdata()
    Time.getdata()
    Time.gettime()
    Space.getdata()
    Space.gettime()
    Space.getspace()
    
    
###### bank account ######

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


if __name__ == "__main__":
    
    myacc = bankaccount("omkar", 20000)
    myacc.deposit(1000)
    
    print(myacc.getbalance())
    
    myacc.withdraw(500)
    print(myacc.getbalance())
    

### private attributes adn methods ###

class person():
    def __init__(self, name, age=30):
        self.name = name
        self.__age = age # private attribute
    def displayinfo(self):
        name = self.name
        age = self.__age
        print("my name is" , name , "and my age is", age)

myObj = person("omkar")
myObj.displayinfo()
print(myObj.name) 
# print(myObj.__age)
### how to access private attributes and methods ###
## print(myObj._person.__age) but should not do it
print(myObj._person__age)

