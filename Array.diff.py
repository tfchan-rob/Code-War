#!/usr/bin/env python
# coding: utf-8

# # Array.diff

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b keeping their order.

# example:
#     
# array_diff([1,2],[1]) == [2]
# 
# If a value is present in b, all of its occurrences must be removed from the other:
# 
# array_diff([1,2,2,2,3],[2]) == [1,3]

# ## my solution

# In[11]:


def array_diff(a, b):
    
    new = []
    
    for num in a:
        if num not in b:
            new.append(num)
    return new


# In[ ]:




