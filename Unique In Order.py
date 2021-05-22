#!/usr/bin/env python
# coding: utf-8

# # Unique In Order

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
# 
# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# 
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# 
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# ## my solution

# In[1]:


def unique_in_order(iterable):
    
    wordlist = []
    letter = None
    
    for i in iterable:
        if i != letter:
            wordlist.append(i)
            letter = i
            
    return wordlist


# In[ ]:



