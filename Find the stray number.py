#!/usr/bin/env python
# coding: utf-8

# # Find the stray number

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# 
# Complete the method which accepts such an array, and returns that single different number.
# 
# The input array will always be valid! (odd-length >= 3)

# example:
# 
# [1, 1, 2] ==> 2
# 
# [17, 17, 3, 17, 17, 17, 17] ==> 3

# ## my solution

# In[7]:


def stray(arr):
    
    for i in arr:
        if arr.count(i) <= 1:
            return i


# In[ ]:




