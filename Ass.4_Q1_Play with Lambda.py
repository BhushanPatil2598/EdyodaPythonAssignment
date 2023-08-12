#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# 
# 
# sample input: 10
# 
# sample output: 35

# In[20]:


def make_adder(x):
    return lambda y: x + y
add5 = make_adder(25)
print(add5(10))


# In[ ]:




