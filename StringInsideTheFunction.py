#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to reverse a string.
# 
# 
# ﻿Sample String : "1234abcd"
# 
# Expected Output : "dcba4321

# In[1]:


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))


# In[ ]:




