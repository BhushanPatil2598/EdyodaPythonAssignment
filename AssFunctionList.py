#!/usr/bin/env python
# coding: utf-8

# # Write a Python function to sum all the numbers in a list.
# 
# 
# Sample List : (8, 2, 3, 0, 7)
# 
# Expected Output : 20
# 
# 
# Explanation:
# 
# 
# Summation should like 8+2+3+0+7 = 20

# In[1]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# In[ ]:




