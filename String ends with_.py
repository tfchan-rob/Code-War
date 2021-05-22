#!/usr/bin/env python
# coding: utf-8

# # String ends with?

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# example:
# 
# solution('abc', 'bc') # returns true
# 
# solution('abc', 'd') # returns false

# ## my solution

# In[3]:


def solution(string, ending):
    
    if ending == str(''):
        return True
    
    for w in ending:
        if w not in string:
            return False
        elif ending[-1] != string[-1]:
            return False
        elif ending not in string:
            return False
        else:
            return True


# In[ ]:




