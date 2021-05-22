#!/usr/bin/env python
# coding: utf-8

# # Descending Order

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# example:
# 
# Input: 42145 Output: 54421
# 
# Input: 145263 Output: 654321
# 
# Input: 123456789 Output: 987654321

# ## my solution

# In[9]:


def descending_order(num):
    string = str(num)
    str_list = []
    new = ''
    
    for w in string:
        str_list.append(w)
        
    str_list.sort()
    str_list.reverse()
    
    for i in str_list:
        new = new+i
    
    return int(new)


# In[ ]:




