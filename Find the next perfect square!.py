#!/usr/bin/env python
# coding: utf-8

# # Find the next perfect square!

# You might know some pretty large perfect squares. But what about the NEXT one?
# 
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# 
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# example:
# 
# findNextSquare(121) --> returns 144
# 
# findNextSquare(625) --> returns 676
# 
# findNextSquare(114) --> returns -1 since 114 is not a perfect square

# ## my solution

# In[5]:


def find_next_square(sq):
    
    result = sq ** 0.5
    
    if (sq % result) == 0 :
        return ((sq**0.5) + 1) ** 2
    else:
        return -1


# In[ ]:




