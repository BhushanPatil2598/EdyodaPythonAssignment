#!/usr/bin/env python
# coding: utf-8

# 
# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[2]:


def findPairs(lst, K):
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))
         
    res.reverse()
    return res
     
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))

Q2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
# In[3]:


def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print(" Updated Reversed list is", A)


# Q3. Write a program to check if two strings are a rotation of each other

# In[4]:


def checkRotation(s1, s2): 
    temp = ''  
    if len(s1) != len(s2): 
        return False
    temp = s1 + s1 
  
    if s2 in temp: 
        return True
    else: 
        return False
   
string1 = "HELLO"
string2 = "LOHEL"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")


# Q4. Write a program to print the first non-repeated character from a string?

# In[7]:


NO_OF_CHARS = [0] * 256

def getCharCountArray(str):
    for i in str:
        NO_OF_CHARS[ord(i)] += 1

def firstNonRepeating(str):
    getCharCountArray(str)
    for i in range(len(str)):
        if NO_OF_CHARS[ord(str[i])] == 1:
            return i
    return -1

str = "PREPINSTA"
index = firstNonRepeating(str)
if index == -1:
    print("No non-repeating character")
else:
    print("First non-repeating character is :", str[index])


# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[10]:


def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from peg {} to peg {}.'.format(source, target))
        return
 
    hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from peg {} to peg {}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)
 
 
disks = int(input('Enter number of disks: '))
hanoi(disks, 'A', 'B', 'C')


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[4]:


def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False

def postToPre(post_exp):
 
    s = []
 
    length = len(post_exp)
 
    for i in range(length):
 
        if (isOperator(post_exp[i])):
 
            
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
           
            temp = post_exp[i] + op2 + op1
 
            s.append(temp)
 
        else:

            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    print("Prefix : ", postToPre(post_exp))


# Q7. Write a program to convert prefix expression to infix expression.

# In[4]:


def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            stack.append(prefix[i])
            i -= 1
        else:
           
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(" infix : ",prefixToInfix(str))


# Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[6]:


def isbalanced(s):
  c= 0
  ans=False
  for i in s:
    if i == "(": 
     c += 1
    elif i == ")":
     c-= 1
    if c < 0:
     return ans
    if c==0:
     return not ans
  return ans
s="{[]}"
print("Given string is balanced :",isbalanced(s))


# Q9. Write a program to reverse a stack.

# In[ ]:


class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        for data in reversed(self.items):
            print(data)
 
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
 
 
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
 
s = Stack()
data_list = input('Please enter the elements to push: ').split()
for data in data_list:
    s.push(int(data))
 
print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()


# Q10. Write a program to find the smallest number using a stack.

# In[1]:


list1 = []
 
num = int(input("Enter number of elements in list: "))
 
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
     
print("Smallest element is:", min(list1))


# In[ ]:




