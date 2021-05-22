#!/usr/bin/env python
# coding: utf-8

# # Count characters in your string

# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# 
# What if the string is empty? Then the result should be empty object literal, {}.

# ## my solution

# In[8]:


def count(string):
    
    return {i : string.count(i) for i in string}


# In[ ]:




