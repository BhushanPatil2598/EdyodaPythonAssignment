#!/usr/bin/env python
# coding: utf-8

# # Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# 
# ﻿Sample String : 'The quick Brow Fox'
# 
# Expected Output :
# 
# No. of Upper case characters : 3
# 
# No. of Lower case Characters : 12

# In[5]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')


# # For Using User Input

# In[7]:


x=input("Enter the string:- ")
def char(x):
  u=0
  l=0
  for i in x:
      if i>='a' and i<='z':
       l+=1

      if i >='A' and i<='Z':
       u+=1

  print("No. Of Upper Case Characters",u)
  print("No. Of Lower Case Characters",l)
char(x)


# In[ ]:




