#!/usr/bin/env python
# coding: utf-8

# # Square Every Digit

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# 
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# 
# Note: The function accepts an integer and returns an integer

# ## my solution

# In[1]:


def square_digits(num):
    
    result = ''
    for i in str(num):
        result += str(int(i)**2)
        
    return int(result)


# In[ ]:




