#!/usr/bin/env python
# coding: utf-8

# # Isograms

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# 
# is_isogram("aba" ) == false
# 
# is_isogram("moOse" ) == false # -- ignore letter case

# ## my solution

# In[2]:


def is_isogram(string):

    wordlist = ''
    
    for w in string.lower():
        if w not in wordlist:
            wordlist += w
        else:
            return False
        
    return True


# In[ ]:




