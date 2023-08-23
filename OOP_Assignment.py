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


class Calculator:

    def __init__(self):
        pass
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass

Challenge 3: Implement the Co
mplete Student Class
# In[7]:


class Student:

    def setName(self):
        pass
    def getName(self):
        pass
    def setRollNumber(self):
        pass
    def getRollNumber(self):
        pass

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

