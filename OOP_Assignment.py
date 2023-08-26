#!/usr/bin/env python
# coding: utf-8
# Challenge 1: Square Numbers and Return Their Sum
# In[5]:


class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        self=int(input("Enter value of num: "))
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) 
        print(self)


Challenge 2: Implement a Calculator Class
# In[6]:
class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num1/self.num2
   
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
obj=calculator(num1,num2)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result:---------->>>>>",obj.add())
    elif choice==2:
        print("Result:---------->>>>> ",obj.subtract())
    elif choice==3:
        print("Result:---------->>>>> ",obj.multiply())
    elif choice==4:
        print("Result:---------->>>>> ",obj.divide())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!") 
print()


Challenge 3: Implement the Co
mplete Student Class
# In[7]:
class Student:
    def __init__(self, Name, RollNumber):
        # private member
        self.Name = Name
        
        self. RollNumber =  RollNumber

    def show(self):
        print('Student Details:', self.Name, self. RollNumber)

    # getter methods
    def get_RollNumber(self):
        return self.RollNumber

    # setter method 
    def set_RollNumber(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.RollNumber = RollNumber

Bhushan = Student('Bhushan', 10, 15)
Bhushan.show()
# changing roll number using setter
Bhushan.set_RollNumber(120)


Bhushan.set_roll_no(25)
Bhushan.show()

Challenge 4: Implement a Banking Account
# In[8]:


class Account:

    def __init__(self):
        # write your code here
        pass

class SavingsAccount():

    def __init__(self):
        # write your code here
        Pass

Challenge 5: Handling a Bank Account
# In[ ]:


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        # write code here
        pass

    def deposit(self, amount):
        # write code here
        pass
    def getBalance(self):
        # write code here
        pass

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        # write code here
        pass

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object

